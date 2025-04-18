import os
import uvicorn
from fastapi import FastAPI
from dotenv import load_dotenv

from config.cors_config import CorsConfig

from hello.controller.hello_controller import helloRouter

load_dotenv()

app = FastAPI()

CorsConfig.middlewareConfig(app)

app.include_router(helloRouter)

if __name__ == "__main__":
    uvicorn.run(app, host=os.getenv('HOST'), port=int(os.getenv('FASTAPI_PORT')))


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
