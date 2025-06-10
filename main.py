from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.endpoints import upload, score, jd

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(upload.router, prefix="/upload")
app.include_router(score.router, prefix="/score")
app.include_router(jd.router, prefix="/jd")

@app.get("/")
def root():
    return {"msg": "CV Scoring API is live 🚀"}
