from pydantic import ConfigDict, BaseModel
from datetime import date
from models.weekly_report import WeeklyReport

class WeeklyReportBase(BaseModel):
    week_number: int
    base_date: date
    this_week: str
    next_week: str
    member_id: int

class WeeklyReportCreate(WeeklyReportBase):
    def to_model(self):
        weekly_report = WeeklyReport(
            week_number=self.week_number,
            base_date=self.base_date,
            this_week=self.this_week, 
            next_week=self.next_week, 
            member_id=self.member_id)
        return weekly_report
    pass

class WeeklyReportUpdate(WeeklyReportBase):
    def update_model(self, weekly_report: WeeklyReport):
        weekly_report.week_number= self.week_number
        weekly_report.base_date = self.base_date
        weekly_report.this_week = self.this_week
        weekly_report.next_week = self.next_week
        weekly_report.member_id = self.member_id
        return
    pass

class WeeklyReportResponse(WeeklyReportBase):
    id: int

    model_config = ConfigDict(from_attributes=True)