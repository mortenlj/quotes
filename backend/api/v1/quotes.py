import random

from fastapi import APIRouter, Depends, HTTPException

from api.deps import get_db
from api.schemas import Quote

router = APIRouter(
    responses={404: {"detail": "Not found"}},
)


@router.get(
    "/",
    response_model=Quote,
)
def get_random_quote(db: dict = Depends(get_db)):
    """Get random quote"""
    return random.choice(db)


@router.get(
    "/{id}",
    response_model=Quote,
)
def get_quote(id: int, db: dict = Depends(get_db)):
    quote = db.get(id)
    if quote is None:
        raise HTTPException(status_code=404, detail="Quote not found")
    return quote
