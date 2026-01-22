from fastapi import FastAPI

from api.api import router

app = FastAPI(
    title = 'Edge-Assisted Face Recognition Attendance System',
    version= '0.0.1'
)

app.include_router(router)