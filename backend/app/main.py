from contextlib import asynccontextmanager
from datetime import datetime, timedelta, timezone
from typing import Annotated, Union

from fastapi import Depends, FastAPI, HTTPException, Request, status
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware

from . import crud, schemas
from .auth import (
    authenticate_user,
    create_access_token,
    fake_users_db,
    get_current_active_user,
    oauth2_scheme,
)
from .config import settings
from .db import SessionLocal, engine


async def get_db() -> AsyncSession:
    try:
        db = SessionLocal()
        yield db
    finally:
        await db.close()


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    await engine.dispose()


# During the development mode, the fronetend is served by
# vite on port 5173. It also seems to prioritize
# the IPv6 on a machine that has it.
origins = [
    "http://localhost",
    "http://127.0.0.1",
    "http://[::1]",
    "http://[::]",
    "http://loclhost:5173",
    "http://127.0.0.1:5173",
    "http://[::1]:5173",
    "http://[::]:5173",
]
middleware = [
    Middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_origin_regex="http[s]://.*\.app\.github\.dev",
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
]
app = FastAPI(middleware=middleware, lifespan=lifespan)


@app.exception_handler(NoResultFound)
async def no_result_found_exception_handler(request: Request, exec: NoResultFound):
    """Global catch-all for SQLAlchemy's NoResultFound."""
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={"message": "Requested item is not found."},
    )


@app.get("/")
async def read_root(token: Annotated[str, Depends(oauth2_scheme)]):
    return {"msg": "hello world"}


@app.get("/users/me")
async def read_users_me(
    current_user: Annotated[schemas.User, Depends(get_current_active_user)]
):
    return current_user


@app.post("/token")
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
) -> schemas.Token:
    user = authenticate_user(fake_users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=settings.access_token_expire_minutes)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return schemas.Token(access_token=access_token, token_type="bearer")


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None]):
    return {"item_id": item_id, "q": q}


@app.get("/classrooms/")
async def get_classrooms(
    current_user: Annotated[schemas.User, Depends(get_current_active_user)],
    skip: int = 0,
    limit: int = 100,
    db: AsyncSession = Depends(get_db),
):
    return await crud.get_classrooms(db, skip, limit)


@app.post("/classrooms/", status_code=status.HTTP_201_CREATED)
async def create_classroom(
    current_user: Annotated[schemas.User, Depends(get_current_active_user)],
    classroom: schemas.ClassroomCreate,
    db: AsyncSession = Depends(get_db),
):
    db_obj = await crud.create_classroom(db, classroom)
    return db_obj


@app.get("/classrooms/{classroom_id}")
async def get_classroom_detail(
    classroom_id: int,
    current_user: Annotated[schemas.User, Depends(get_current_active_user)],
    db: AsyncSession = Depends(get_db),
    response_model=schemas.Classroom,
):
    return await crud.get_classroom(db, classroom_id)


@app.patch("/classrooms/{classroom_id}")
async def update_classrooms(
    classroom_id: int,
    classroom: schemas.ClassroomUpdate,
    current_user: Annotated[schemas.User, Depends(get_current_active_user)],
    db: AsyncSession = Depends(get_db),
):
    print("update classroom")
    return await crud.update_classroom(db, classroom_id, classroom)


@app.delete("/classrooms/{classroom_id}")
async def delete_classroom(
    classroom_id: int,
    current_user: Annotated[schemas.User, Depends(get_current_active_user)],
    db: AsyncSession = Depends(get_db),
):
    return await crud.delete_classroom(db, classroom_id)


@app.post(
    "/classrooms/{classroom_id}/import/students-from-bb",
    status_code=status.HTTP_200_OK,
)
async def import_students_from_bb(
    classroom_id: int,
    membership_results: schemas.MembershipResult,
    current_user: Annotated[schemas.User, Depends(get_current_active_user)],
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
    current_user: Annotated[schemas.User, Depends(get_current_active_user)],
    db: AsyncSession = Depends(get_db),
):
    return await crud.get_students(db, classroom_id)


@app.get("/classrooms/{classroom_id}/students/{student_id}")
async def get_student(
    classroom_id: int,
    student_id: int,
    current_user: Annotated[schemas.User, Depends(get_current_active_user)],
    db: AsyncSession = Depends(get_db),
):
    return await crud.get_student(db, classroom_id, student_id)
