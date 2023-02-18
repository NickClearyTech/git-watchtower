from fastapi import FastAPI
import watchtower.routers.repository as repo

app = FastAPI()
app.include_router(repo.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}
