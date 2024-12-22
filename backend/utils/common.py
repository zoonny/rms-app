

# 주차 정보 출력
week_info = get_week_info()
print("Today's Date:", week_info["today"])
print("Year:", week_info["year"])
print("Week Number:", week_info["week_number"])
print("Weekday (1=Monday, 7=Sunday):", week_info["weekday"])