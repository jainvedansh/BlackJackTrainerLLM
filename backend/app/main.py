from fastapi import FastAPI
from app.api.rounds import router as rounds_router

app = FastAPI()


@app.get("/health")
def health_check():
    return {"status": "ok"}


app.include_router(rounds_router, prefix="/rounds")
