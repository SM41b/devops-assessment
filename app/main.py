from fastapi import FastAPI

app = FastAPI(title="DevOps Assessment API")


@app.get("/")
def root():
    return {"message": "DevOps Assessment API is running"}


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.get("/hello/{name}")
def hello(name: str):
    return {"message": f"Hello, {name}!"}