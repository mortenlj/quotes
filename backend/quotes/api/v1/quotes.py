import random

from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import RedirectResponse
from starlette import status

from quotes.api.deps import get_db
from quotes.api.schemas import Quote

router = APIRouter(
    responses={404: {"detail": "Not found"}},
)


@router.get("/", status_code=status.HTTP_303_SEE_OTHER)
def get_random_quote(db: dict = Depends(get_db)):
    """Get random quote"""
    quote_id = random.choice(list(db.keys()))
    url = router.url_path_for("get_quote", id=quote_id)
    return RedirectResponse(url=f".{url}", status_code=status.HTTP_303_SEE_OTHER)


@router.get(
    "/{id}",
    response_model=Quote,
)
def get_quote(id: int, db: dict = Depends(get_db)):
    quote = db.get(id)
    if quote is None:
        raise HTTPException(status_code=404, detail="Quote not found")
    return quote
