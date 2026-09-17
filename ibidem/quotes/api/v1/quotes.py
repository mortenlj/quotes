import random
from typing import Annotated

from fastapi import APIRouter, Depends, Header, HTTPException
from fastapi.responses import PlainTextResponse, RedirectResponse
from starlette import status

from ibidem.quotes.api.schemas import Quote
from ibidem.quotes.deps import get_db

router = APIRouter(
    responses={404: {"detail": "Not found"}},
)


@router.get("/", status_code=status.HTTP_303_SEE_OTHER)
def get_random_quote(db: Annotated[dict, Depends(get_db)]):
    """Get random quote"""
    quote_id = random.choice(list(db.keys()))
    url = router.url_path_for("get_quote", id=quote_id)
    return RedirectResponse(url=f".{url}", status_code=status.HTTP_303_SEE_OTHER)


@router.get(
    "/{id}",
    response_model=Quote,
)
def get_quote(
    id: int,
    db: Annotated[dict, Depends(get_db)],
    accept: Annotated[str | None, Header()] = "application/json",
    user_agent: Annotated[str | None, Header()] = None,
):
    quote = db.get(id)
    if quote is None:
        raise HTTPException(status_code=404, detail="Quote not found")
    if accept == "text/plain" or user_agent.startswith("xscreensaver-text"):
        return PlainTextResponse(quote)
    return quote
