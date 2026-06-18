from pydantic import BaseModel, Field
from enum import Enum



class NewMission(BaseModel):
    title: str
    description: str
    location: str
    difficulty: int = Field(..., ge=1, le=10)
    importance: int = Field(..., ge=1, le=10)

class UpdateAgent(BaseModel):
    title: str | None = None
    description: str | None = None
    location: str | None = None
    difficulty: str | None = None
    importance: int | None = None

