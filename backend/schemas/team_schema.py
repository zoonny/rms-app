from pydantic import ConfigDict, BaseModel
from models.team import Team

class TeamBase(BaseModel):
    name: str

class TeamCreate(TeamBase):
    def to_model(self):
        team = Team(
            name=self.name)
        return team
    pass

class TeamUpdate(TeamBase):
    def update_model(self, team: Team):
        team.name = self.name
        return
    pass

class TeamResponse(TeamBase):
    id: int

    model_config = ConfigDict(from_attributes=True)