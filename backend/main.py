from fastapi import FastAPI, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
import watchtower.routers.repository as repo

app = FastAPI()
app.include_router(repo.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}
