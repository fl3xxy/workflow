from fastapi import FastAPI
from src.routes.get_current_day_of_week import router

app = FastAPI()

app.include_router(router)