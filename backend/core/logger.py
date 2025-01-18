import logging

# logger
logger = logging.getLogger("rms-app")
logger.setLevel(logging.DEBUG)  # 로그 레벨 설정

# 콘솔 핸들러 생성 및 설정
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_formatter = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s')
console_handler.setFormatter(console_formatter)

# 파일 핸들러 생성 및 설정
# file_handler = logging.FileHandler('app.log')
# file_handler.setLevel(logging.INFO)
# file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# file_handler.setFormatter(file_formatter)

# 로거에 핸들러 추가
logger.addHandler(console_handler)
# logger.addHandler(file_handler)
