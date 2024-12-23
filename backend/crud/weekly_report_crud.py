from sqlalchemy.orm import Session
from models.weekly_report import WeeklyReport 
from schemas.weekly_report_schema import WeeklyReportCreate, WeeklyReportUpdate

class WeeklyReportCRUD:
    def get_weekly_reports(self, db: Session, skip: int = 0, limit: int = 10):
        return db.query(WeeklyReport).offset(skip).limit(limit).all()

    def get_weekly_report(self, db: Session, weekly_report_id: int):
        return db.query(WeeklyReport).filter(WeeklyReport.id == weekly_report_id).first()

    def create_weekly_report(self, db: Session, weekly_report: WeeklyReportCreate):
        db_weekly_report = weekly_report.to_model()
        db.add(db_weekly_report)
        db.commit()
        db.refresh(db_weekly_report)
        return db_weekly_report

    def update_weekly_report(self, db: Session, weekly_report_id: int, weekly_report: WeeklyReportUpdate):
        db_weekly_report = db.query(WeeklyReport).filter(WeeklyReport.id == weekly_report_id).first()
        if db_weekly_report:
            weekly_report.update_model(db_weekly_report)
            db.commit()
            db.refresh(db_weekly_report)
        return db_weekly_report

    def delete_weekly_report(self, db: Session, weekly_report_id: int):
        db_weekly_report = db.query(WeeklyReport).filter(WeeklyReport.id == weekly_report_id).first()
        if db_weekly_report:
            db.delete(db_weekly_report)
            db.commit()
        return db_weekly_report