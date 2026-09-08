from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI(title="DevOps Assessment API")

Instrumentator().instrument(app).expose(app)


@app.get("/")
def root():
    return {"message": "DevOps Assessment API is running"}


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.get("/hello/{name}")
def hello(name: str):
    return {"message": f"Hello, {name}!"}