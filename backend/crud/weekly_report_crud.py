from sqlalchemy.orm import Session
from models.weekly_report import WeeklyReport 
from schemas.weekly_report_schema import WeeklyReportCreate, WeeklyReportUpdate

class WeeklyReportCRUD:
    def get_weekly_reports(self, db: Session, skip: int = 0, limit: int = 10):
        return db.query(WeeklyReport).offset(skip).limit(limit).all()

    def get_weekly_report(self, db: Session, weekly_report_id: int):
        return db.query(WeeklyReport).filter(WeeklyReport.id == weekly_report_id).first()

    def create_weekly_report(self, db: Session, weekly_report: WeeklyReportCreate):
        # db_weekly_report = WeeklyReport(week_number=weekly_report.week_number, base_date=weekly_report.base_date,
        #                                  this_week=weekly_report.this_week, next_week=weekly_report.next_week,
        #                                  member_id=weekly_report.member_id)
        db_weekly_report = weekly_report.to_weekly_report()
        db.add(db_weekly_report)
        db.commit()
        db.refresh(db_weekly_report)
        return db_weekly_report

    def update_weekly_report(self, db: Session, weekly_report_id: int, weekly_report: WeeklyReportUpdate):
        db_weekly_report = db.query(WeeklyReport).filter(WeeklyReport.id == weekly_report_id).first()
        if db_weekly_report:
            # db_weekly_report.week_number= weekly_report.week_number
            # db_weekly_report.base_date = weekly_report.base_date
            # db_weekly_report.this_week = weekly_report.this_week
            # db_weekly_report.next_week = weekly_report.next_week
            # db_weekly_report.member_id = weekly_report.member_id
            weekly_report.from_weekly_report(db_weekly_report)
            db.commit()
            db.refresh(db_weekly_report)
        return db_weekly_report

    def delete_weekly_report(self, db: Session, weekly_report_id: int):
        db_weekly_report = db.query(WeeklyReport).filter(WeeklyReport.id == weekly_report_id).first()
        if db_weekly_report:
            db.delete(db_weekly_report)
            db.commit()
        return db_weekly_report