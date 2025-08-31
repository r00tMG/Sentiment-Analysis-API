from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from router import home, huggingFace

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key="ton_secret_ultra_securise")

app.include_router(home.router)
app.include_router(huggingFace.router)