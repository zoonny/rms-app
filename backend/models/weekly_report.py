from sqlalchemy import Column, Integer, String, Date
from models.base import BaseModel

class WeeklyReport(BaseModel):
    __tablename__ = "weekly_reports"

    id = Column(Integer, primary_key=True, index=True)
    week_number = Column(Integer, nullable=False)
    base_date = Column(Date, nullable=False)
    this_week = Column(String, nullable=False)
    next_week = Column(String, nullable=False)
    # start_date = Column(Date, nullable=False)
    # end_date = Column(Date, nullable=False)