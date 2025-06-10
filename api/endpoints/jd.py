from fastapi import APIRouter
from api.schemas import Job

router = APIRouter()

@router.get("/", response_model=list[Job])
def get_jobs():
    return [
        Job(id=1, title="AI Engineer", jd="Experience in ML, Python, LLM..."),
        Job(id=2, title="Frontend Developer", jd="React, Tailwind, REST API...")
    ]

