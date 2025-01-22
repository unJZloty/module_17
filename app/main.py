from fastapi import FastAPI
from app.routers import task, user

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to Taskmanager"}

app.include_router(user.router)
app.include_router(task.router)
