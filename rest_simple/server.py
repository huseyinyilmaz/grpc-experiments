from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/increase/{number}")
async def read_item(number: int):
    return {"number": number+1 }
