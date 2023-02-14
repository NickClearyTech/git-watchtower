from fastapi import FastAPI
from watchtower.thingy import a_func

app = FastAPI()


@app.get("/")
async def root():
    a_func()
    return {"message": "Hello World"}

def a_func2():
    print("hi")