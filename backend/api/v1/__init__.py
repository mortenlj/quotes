from fastapi import APIRouter

from . import quotes

router = APIRouter()
router.include_router(quotes.router, prefix="/quotes", tags=["quotes"])
