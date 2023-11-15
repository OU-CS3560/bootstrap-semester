"""
Wait for the database.

Usually, a database container server will take time to start up.

Exit codes:
- 0 Database is read
- 1 Database is not ready or any error occur.s
"""
import sys
import random
import asyncio
from sqlalchemy import select

from .db import engine, SessionLocal

FAILURE_COUNT_LIMIT = 10

async def main():
    failure_count = 0
    not_ready = True

    while not_ready:
        try:
            async with SessionLocal() as session:
                result = await session.execute(select(1))
                if result.one()[0] == 1:
                    not_ready = False
                    print(f"[wait_db]: database is ready")
        except Exception:
            not_ready = True
            failure_count += 1
            print(f"[wait_db]: fail to connect to database at '{engine.url.host}' (failure count: {failure_count})")

        if failure_count > FAILURE_COUNT_LIMIT:
            print(f"[wait_db]: failure count ({failure_count}) exceed the limit ({FAILURE_COUNT_LIMIT})")
            sys.exit(1)
        
        # See https://cloud.google.com/memorystore/docs/redis/exponential-backoff#example_algorithm
        await asyncio.sleep((2.0 ** failure_count) + random.random())

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
