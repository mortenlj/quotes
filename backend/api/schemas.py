from typing import Optional

from pydantic import ConfigDict
from pydantic.main import BaseModel


class Quote(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    quote: str
    dedication: Optional[str] = None
