from sqlalchemy.orm import Session
from crud.weekly_report_crud import WeeklyReportCRUD
from schemas.weekly_report_schema import WeeklyReportCreate, WeeklyReportUpdate

class WeeklyReportService:
    def __init__(self, db: Session, crud: WeeklyReportCRUD):
        self.db = db
        self.crud = crud

    def list_weekly_reports(self, skip: int = 0, limit: int = 10):
        return self.crud.get_weekly_reports(self.db, skip=skip, limit=limit)

    def get_weekly_report(self, weekly_report_id: int):
        weekly_report = self.crud.get_weekly_report(self.db, weekly_report_id=weekly_report_id)
        if not weekly_report:
            raise ValueError("weekly_report not found")
        return weekly_report 

    def create_weekly_report(self, weekly_report: WeeklyReportCreate):
        return self.crud.create_weekly_report(self.db, weekly_report=weekly_report)

    def update_weekly_report(self, weekly_report_id: int, weekly_report: WeeklyReportUpdate):
        return self.crud.update_weekly_report(self.db, weekly_report_id=weekly_report_id, weekly_report=weekly_report)

    def delete_weekly_report(self, weekly_report_id: int):
        return self.crud.delete_weekly_report(self.db, weekly_report_id=weekly_report_id)