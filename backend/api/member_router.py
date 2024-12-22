from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.member_schema import MemberCreate, MemberUpdate, MemberResponse
from db.database import get_db
from services.member_service import MemberService
from crud.member_crud import MemberCRUD

router = APIRouter()

def get_member_service(db: Session = Depends(get_db)):
    crud = MemberCRUD()
    return MemberService(db=db, crud=crud)

@router.get("/members", response_model=list[MemberResponse])
def read_members(skip: int = 0, limit: int = 10, member_service: MemberService = Depends(get_member_service)):
    return member_service.list_members(skip=skip, limit=limit)

@router.get("/members/{member_id}", response_model=MemberResponse)
def read_member(member_id: int, member_service: MemberService = Depends(get_member_service)):
    try:
        return member_service.get_member(member_id=member_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.post("/members", response_model=MemberResponse)
def create_new_member(member: MemberCreate, member_service: MemberService = Depends(get_member_service)):
    try:
        return member_service.create_member(member=member)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.put("/members/{member_id}", response_model=MemberResponse)
def update_existing_member(member_id: int, member: MemberUpdate, member_service: MemberService = Depends(get_member_service)):
    try:
        return member_service.update_member(member_id, member)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/members/{member_id}")
def delete_existing_member(member_id: int, member_service: MemberService = Depends(get_member_service)):
    try:
        return member_service.delete_member(member_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))