from sqlalchemy.orm import Session
from crud.team_crud import TeamCRUD
from schemas.team_schema import TeamCreate, TeamUpdate

class TeamService:
    def __init__(self, db: Session, crud: TeamCRUD):
        self.db = db
        self.crud = crud

    def list_teams(self, skip: int = 0, limit: int = 10):
        return self.crud.get_teams(self.db, skip=skip, limit=limit)

    def get_team(self, team_id: int):
        team = self.crud.get_team(self.db, team_id=team_id)
        if not team:
            raise ValueError("team not found")
        return team 

    def create_team(self, team: TeamCreate):
        return self.crud.create_team(self.db, team=team)

    def update_team(self, team_id: int, team: TeamUpdate):
        return self.crud.update_team(self.db, team_id=team_id, team=team)

    def delete_team(self, team_id: int):
        return self.crud.delete_team(self.db, team_id=team_id)