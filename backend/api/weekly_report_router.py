from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.weekly_report_schema import WeeklyReportCreate, WeeklyReportUpdate, WeeklyReportResponse
from db.database import get_db
from services.weekly_report_service import WeeklyReportService
from crud.weekly_report_crud import WeeklyReportCRUD

router = APIRouter()

def get_weekly_report_service(db: Session = Depends(get_db)):
    crud = WeeklyReportCRUD()
    return WeeklyReportService(db=db, crud=crud)

@router.get("/weekly_reports", response_model=list[WeeklyReportResponse])
def read_weekly_reports(skip: int = 0, limit: int = 10, weekly_report_service: WeeklyReportService = Depends(get_weekly_report_service)):
    return weekly_report_service.list_weekly_reports(skip=skip, limit=limit)

@router.get("/weekly_reports/{weekly_report_id}", response_model=WeeklyReportResponse)
def read_weekly_report(weekly_report_id: int, weekly_report_service: WeeklyReportService = Depends(get_weekly_report_service)):
    try:
        return weekly_report_service.get_weekly_report(weekly_report_id=weekly_report_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.post("/weekly_reports", response_model=WeeklyReportResponse)
def create_new_weekly_report(weekly_report: WeeklyReportCreate, weekly_report_service: WeeklyReportService = Depends(get_weekly_report_service)):
    try:
        return weekly_report_service.create_weekly_report(weekly_report=weekly_report)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.put("/weekly_reports/{weekly_report_id}", response_model=WeeklyReportResponse)
def update_existing_weekly_report(weekly_report_id: int, weekly_report: WeeklyReportUpdate, weekly_report_service: WeeklyReportService = Depends(get_weekly_report_service)):
    try:
        return weekly_report_service.update_weekly_report(weekly_report_id, weekly_report)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/weekly_reports/{weekly_report_id}")
def delete_existing_weekly_report(weekly_report_id: int, weekly_report_service: WeeklyReportService = Depends(get_weekly_report_service)):
    try:
        return weekly_report_service.delete_weekly_report(weekly_report_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))