import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from utils.delete_output_files import delete_files_in_output
from routers import images, video

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    '*',
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def config_router(app):
    app.include_router(images.router)
    app.include_router(video.router)


config_router(app)

if __name__ == "__main__":
    delete_files_in_output()
    uvicorn.run(app, host="localhost", port=8000)
