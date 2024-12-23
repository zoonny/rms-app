from datetime import datetime

def get_week_info():
    # 현재 날짜
    today = datetime.now()

    # ISO 표준 기준 연도, 주차, 요일 정보 얻기
    year, week, weekday = today.isocalendar()

    return {
        "year": year,
        "week_number": week,
        "weekday": weekday,  # 1=Monday, 7=Sunday
        "today": today.strftime("%Y-%m-%d")  # YYYY-MM-DD 형식으로 출력
    }

# 주차 정보 출력
week_info = get_week_info()
print("Today's Date:", week_info["today"])
print("Year:", week_info["year"])
print("Week Number:", week_info["week_number"])
print("Weekday (1=Monday, 7=Sunday):", week_info["weekday"])

