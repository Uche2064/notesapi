from fastapi import FastAPI
from routers import user, notes
app = FastAPI()

app.include_router(user.router)
app.include_router(notes.router)

