from fastapi import APIRouter, Body
from api.schemas import ScoreRequest, ScoreResponse
from api.services.cv_scorer import CVScorer

router = APIRouter()

@router.post("/", response_model=ScoreResponse)
async def score(request: ScoreRequest):
    scorer = CVScorer()
    score_value = scorer.score(request.cv_text, request.jd_text)
    return ScoreResponse(score=score_value)
