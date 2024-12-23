from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.team_schema import TeamCreate, TeamUpdate, TeamResponse
from db.database import get_db
from services.team_service import TeamService
from crud.team_crud import TeamCRUD

router = APIRouter()

def get_team_service(db: Session = Depends(get_db)):
    crud = TeamCRUD()
    return TeamService(db=db, crud=crud)

@router.get("/teams", response_model=list[TeamResponse])
def read_teams(skip: int = 0, limit: int = 10, team_service: TeamService = Depends(get_team_service)):
    return team_service.list_teams(skip=skip, limit=limit)

@router.get("/teams/{team_id}", response_model=TeamResponse)
def read_team(team_id: int, team_service: TeamService = Depends(get_team_service)):
    try:
        return team_service.get_team(team_id=team_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.post("/teams", response_model=TeamResponse)
def create_new_team(team: TeamCreate, team_service: TeamService = Depends(get_team_service)):
    try:
        return team_service.create_team(team=team)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.put("/teams/{team_id}", response_model=TeamResponse)
def update_existing_team(team_id: int, team: TeamUpdate, team_service: TeamService = Depends(get_team_service)):
    try:
        return team_service.update_team(team_id, team)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/teams/{team_id}")
def delete_existing_team(team_id: int, team_service: TeamService = Depends(get_team_service)):
    try:
        return team_service.delete_team(team_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))