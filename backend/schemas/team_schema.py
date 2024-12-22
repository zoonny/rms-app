from pydantic import ConfigDict, BaseModel

class TeamBase(BaseModel):
    name: str

class TeamCreate(TeamBase):
    pass

class TeamUpdate(TeamBase):
    pass

class TeamResponse(TeamBase):
    id: int

    model_config = ConfigDict(from_attributes=True)