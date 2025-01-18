from datetime import date, timedelta
from holidayskr import year_holidays

holidays = [
    '2025-01-22',
    '2025-01-23',
    '2025-01-24'
]

def get_working_days(year, month):
    # 해당 월의 첫 번째 날과 마지막 날 계산
    first_day = date(year, month, 1)
    if month == 12:
        last_day = date(year + 1, 1, 1) - timedelta(days=1)
    else:
        last_day = date(year, month + 1, 1) - timedelta(days=1)

    # 해당 연도의 공휴일 목록 가져오기
    holidays = {holiday for holiday, _ in year_holidays(year)}

    # 근무일 목록 생성
    working_days = []
    current_day = first_day
    while current_day <= last_day:
        # 월요일(0)부터 금요일(4)까지가 평일이며, 공휴일이 아닌 날을 근무일로 간주
        if current_day.weekday() < 5 and current_day not in holidays:
            working_days.append(current_day)
        current_day += timedelta(days=1)

    return working_days

def filter_holiday(days, holidays):
    # holidays 리스트에서 제거할 days 리스트
    return [item for item in holidays if item != days]

# 사용 예시
year = 2025
month = 1
days = get_working_days(year, month)
# for day in days:
#     print(day)

working_days = filter_holiday(days, holidays)
for working_day in working_days:
    print(type(working_day), working_day)

# 나쁜코드
sources = [1, 2, 3, 4]
filters = [2, 3]

def find_item(findItem, items):
    finded = False
    for item in items:
        if item == findItem:
            finded = True
            break
    return finded

bucket: list = []
for item in sources:
    if find_item(item, filters) == False:
        bucket.append(item)

print(bucket)

# 좋은코드
sources = [1, 2, 3, 4]
filters = [2, 3]

bucket = [item for item in sources if item not in filters]

print(bucket)

import utils.auth

pwd = 'new1234!'
hash = utils.auth.hash_password(pwd)
print(hash)

print(utils.auth.verify_password(pwd, hash), utils.auth.verify_password('New1234!', hash))

from datetime import timedelta

access_token_expires = timedelta(minutes=utils.auth.ACCESS_TOKEN_EXPIRE_MINUTES)
access_token = utils.auth.create_access_token(data={"sub": "82022284"}, expires_delta=access_token_expires)
print(access_token_expires, access_token)
