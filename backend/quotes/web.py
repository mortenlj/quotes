import random

from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette import status

from quotes.deps import get_db, templates

router = APIRouter()


@router.get("/", status_code=status.HTTP_303_SEE_OTHER)
def get_random_quote(db: dict = Depends(get_db)):
    """Get random quote"""
    quote_id = random.choice(list(db.keys()))
    url = router.url_path_for("get_quote", id=quote_id)
    return RedirectResponse(url=f".{url}", status_code=status.HTTP_303_SEE_OTHER)


@router.get("/{id}", response_class=HTMLResponse)
def get_quote(request: Request, id: int, db: dict = Depends(get_db), templates: Jinja2Templates = Depends(templates)):
    quote = db.get(id)
    if quote is None:
        raise HTTPException(status_code=404, detail="Quote not found")
    return templates.TemplateResponse(request, "quote.html.j2", context={"data": quote})
