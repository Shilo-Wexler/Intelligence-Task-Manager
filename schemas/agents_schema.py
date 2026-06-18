from pydantic import BaseModel
from enum import Enum



class AgentRank(str, Enum):
    junior = 'Junior'
    senior = 'Senior'
    commander = 'Commander'


class NewAgent(BaseModel):
    name: str
    specialty: str
    agent_rank: AgentRank


class UpdateAgent(BaseModel):
    name: str | None = None
    specialty: str | None = None
    agent_rank: AgentRank | None = None