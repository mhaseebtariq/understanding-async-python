import asyncio
import time

from fastapi import FastAPI

app = FastAPI()


@app.get("/external")
async def external() -> int:
    await asyncio.sleep(3)
    return 1


@app.get("/external_sync")
def external_sync() -> int:
    time.sleep(3)
    return 2
