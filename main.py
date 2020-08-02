from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, PlainTextResponse
from fastapi.exceptions import RequestValidationError

app = FastAPI()

items = {"foo": "thinker of the fighter of the decoder"}


class UnicornException(Exception):
    def __init__(self, name: str):
        self.name = name


@app.exception_handler(RequestValidationError)
async def unicorn_exception(request: Request, exc : UnicornException):
    return PlainTextResponse(str(exc), status_code=400)


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    if item_id not in items:
        pass
    return {"theBomb": "Bomber Booty"}
