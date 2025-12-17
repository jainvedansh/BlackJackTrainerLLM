from fastapi import FastAPI
from app.api.rounds import router as rounds_router
from app.core.database import engine, Base
from app.models import round

app = FastAPI()


@app.get("/health")
def health_check():
    return {"status": "ok"}


app.include_router(rounds_router, prefix="/rounds")

Base.metadata.create_all(bind=engine)
