print("새로운 프로젝트")

import os

def printApiKey():
    # 환경 변수 가져오기
    openai_api_key = os.getenv('OPENAI_API_KEY')
    
    # 출력
    if openai_api_key:
        print(f"OPENAI_API_KEY: {openai_api_key}")
    else:
        print("OPENAI_API_KEY 환경 변수가 설정되지 않았습니다.")

# 함수 실행
printApiKey()