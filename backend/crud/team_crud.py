from sqlalchemy.orm import Session
from models.team import Team 
from schemas.team_schema import TeamCreate, TeamUpdate

class TeamCRUD:
    def get_teams(self, db: Session, skip: int = 0, limit: int = 10):
        return db.query(Team).offset(skip).limit(limit).all()

    def get_team(self, db: Session, team_id: int):
        return db.query(Team).filter(Team.id == team_id).first()

    def create_team(self, db: Session, team: TeamCreate):
        db_team = team.to_model()
        db.add(db_team)
        db.commit()
        db.refresh(db_team)
        return db_team

    def update_team(self, db: Session, team_id: int, team: TeamUpdate):
        db_team = db.query(Team).filter(Team.id == team_id).first()
        if db_team:
            team.update_model(db_team)
            db.commit()
            db.refresh(db_team)
        return db_team

    def delete_team(self, db: Session, team_id: int):
        db_team = db.query(Team).filter(Team.id == team_id).first()
        if db_team:
            db.delete(db_team)
            db.commit()
        return db_team