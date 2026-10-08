from fastapi import FastAPI

app = FastAPI(title="Deepdive-ai API")

@app.get("/health")
def health():
    return {"status": "ok"}

# TODO: include routers: videos, ask, generate
