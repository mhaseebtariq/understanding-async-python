import random
import time
import uuid

import httpx
from fastapi import FastAPI

EXTERNAL = "http://127.0.0.1:8001/external"
EXTERNAL_SYNC = "http://127.0.0.1:8001/external_sync"

app = FastAPI()


@app.get("/api/sync")
def sync() -> dict:
    response = httpx.Client().get(f"{EXTERNAL}?rid={uuid.uuid4()}")
    return {"response": response.text}


@app.get("/api/sync__external_sync")
def sync__external_sync() -> dict:
    response = httpx.Client().get(f"{EXTERNAL_SYNC}?rid={uuid.uuid4()}")
    return {"response": response.text}


@app.get("/api/sync_cpu_bound")
def sync_cpu_bound() -> dict:
    start = time.time()
    while True:
        value = max([5, random.randint(1, 10)])
        if (time.time() - start) > 4:
            break
    return {"response": value, "type": "cpu_bound"}


@app.get("/api/async_without_async_code")
async def async_without_async_code() -> dict:
    response = httpx.Client().get(f"{EXTERNAL}?rid={uuid.uuid4()}")
    return {"response": response.text, "id": 0}


@app.get("/api/async_with_async_code_1")
async def async_with_async_code_1() -> dict:
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{EXTERNAL}?rid={uuid.uuid4()}")
    return {"response": response.text, "id": 1}


@app.get("/api/async_with_async_code_2")
async def async_with_async_code_2() -> dict:
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{EXTERNAL}?rid={uuid.uuid4()}")
    return {"response": response.text, "id": 2}
