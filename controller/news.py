from fastapi import APIRouter
from use_case.news import news_pipeline

router = APIRouter(
    prefix="/headlines",
    tags=['HEADLINES']
)

@router.post('/get_headlines')
def get_headlines_controller():
    return news_pipeline()