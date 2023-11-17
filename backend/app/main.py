from typing import Annotated, Union

from fastapi import FastAPI, Depends, status, Request, HTTPException
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import NoResultFound

from . import crud
from .config import settings
from .schemas import MembershipResult, ClassroomCreate, ClassroomUpdate, User, UserInDB
from .db import SessionLocal, engine
from .auth import oauth2_scheme, get_current_active_user, fake_users_db, fake_hash_password


async def get_db() -> AsyncSession:
    try:
        db = SessionLocal()
        yield db
    finally:
        await db.close()

# During the development mode, the fronetend is served by
# vite on port 5173. It also seems to prioritize
# the IPv6 on a machine that has it.
origins = [
    "http://localhost",
    "http://127.0.0.1",
    "http://[::1]",
    "http://loclhost:5173",
    "http://127.0.0.1:5173",
    "http://[::1]:5173",
]
middleware = [
    Middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_origin_regex="http[s]:\/\/.*\.app\.github\.dev",
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
]
app = FastAPI(middleware=middleware)


@app.on_event("startup")
async def startup():
    pass


@app.on_event("shutdown")
async def shutdown():
    await engine.dispose()


@app.exception_handler(NoResultFound)
async def no_result_found_exception_handler(request: Request, exec: NoResultFound):
    """Global catch-all for SQLAlchemy's NoResultFound."""
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={"message": "Requested item is not found."},
    )


@app.get("/")
async def read_root(token: Annotated[str, Depends(oauth2_scheme)]):
    return {"msg": "hello world", "token": token}


@app.get("/users/me")
async def read_users_me(current_user: Annotated[User, Depends(get_current_active_user)]):
    return current_user


@app.post("/token")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user_dict = fake_users_db.get(form_data.username)
    if not user_dict:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    user = UserInDB(**user_dict)
    hashed_password = fake_hash_password(form_data.password)
    print(user, hashed_password)
    if not hashed_password == user.hashed_password:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    return {"access_token": user.username, "token_type": "bearer"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None]):
    return {"item_id": item_id, "q": q}


@app.get("/classrooms/")
async def get_classrooms(
    skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)
):
    return await crud.get_classrooms(db, skip, limit)


@app.post("/classrooms/", status_code=status.HTTP_201_CREATED)
async def create_classroom(
    classroom: ClassroomCreate, db: AsyncSession = Depends(get_db)
):
    db_obj = await crud.create_classroom(db, classroom)
    return db_obj


@app.get("/classrooms/{classroom_id}")
async def get_classrooms(
    classroom_id: int,
    db: AsyncSession = Depends(get_db),
):
    return await crud.get_classroom(db, classroom_id)


@app.patch("/classrooms/{classroom_id}")
async def update_classrooms(
    classroom_id: int,
    classroom: ClassroomUpdate,
    db: AsyncSession = Depends(get_db),
):
    print("update classroom")
    return await crud.update_classroom(db, classroom_id, classroom)

@app.delete("/classrooms/{classroom_id}")
async def delete_classroom(
    classroom_id: int,
    db: AsyncSession = Depends(get_db),
):
    return await crud.delete_classroom(db, classroom_id)


@app.post(
    "/classrooms/{classroom_id}/import/students-from-bb",
    status_code=status.HTTP_200_OK,
)
async def import_students_from_bb(
    classroom_id: int,
    membership_results: MembershipResult,
    db: AsyncSession = Depends(get_db),
):
    try:
        return await crud.import_students_bb(db, classroom_id, membership_results)
    except NoResultFound:
        # Manually catch the exception, so we can provide a better message.
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Classroom (with id={classroom_id}) not found. You are attempting to import students into non-existent Classroom",
        )


@app.get("/classrooms/{classroom_id}/students")
async def get_students(
    classroom_id: int,
    db: AsyncSession = Depends(get_db),
):
    return await crud.get_students(db, classroom_id)


@app.get("/classrooms/{classroom_id}/students/{student_id}")
async def get_student(
    classroom_id: int,
    student_id: int,
    db: AsyncSession = Depends(get_db),
):
    return await crud.get_student(db, classroom_id, student_id)
