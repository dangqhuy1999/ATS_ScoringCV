from pydantic import BaseModel

class UploadResponse(BaseModel):
    filename: str
    status: str

class ScoreRequest(BaseModel):
    cv_text: str
    jd_text: str

class ScoreResponse(BaseModel):
    score: float

class Job(BaseModel):
    id: int
    title: str
    jd: str

