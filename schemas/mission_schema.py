from pydantic import BaseModel, Field
from enum import Enum



class NewMission(BaseModel):
    title: str
    description: str
    location: str
    difficulty: str
    importance: int = Field(..., le=1, ge=10)
    location: int = Field(..., le=1, ge=10)


class UpdateAgent(BaseModel):
    title: str | None = None
    description: str | None = None
    location: str | None = None
    difficulty: str | None = None
    importance: int | None = None
    location: int  | None = None

