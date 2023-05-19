"""
Wait for the database.

Usually database container server will take time to start up.
"""
import asyncio


async def main():
    # FIXME(KC): Implement database wait.
    pass


if __name__ == "__main__":
    loop = asyncio.get_running_loop()
    loop.run_until_complete(main())
