# 학습 json파일 형식{"user": "...", "ai": "..."}

import openai
import json

openai.api_key = "API Key"  # OpenAI API key 설정

# GPT-2 모델에서 사용할 하이퍼파라미터 설정
model_engine = "text-davinci-002"  # 모델 엔진 선택
temperature = 0.7  # 출력 결과 다양성을 조절할 수 있는 옵션. 0.7은 중간 정도입니다.
max_tokens = 100  # 모델이 생성할 최대 토큰 수. 즉, 챗봇이 생성할 최대 단어 수

# 학습 데이터 로드
with open("chatbot_data.json", "r") as f:
    chat_data = json.load(f)


# GPT-2 API로 모델 학습하기
def train_gpt2(chat_data):
    prompt = ""
    for chat in chat_data:
        # 사용자의 입력과 모델이 생성한 응답을 하나의 프롬프트로 합침
        prompt += f"User: {chat['user']}\nAI: {chat['ai']}\n"

    # GPT-2 API를 사용하여 학습을 진행
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        temperature=temperature,
        max_tokens=max_tokens,
        n=1,
        stop=None,
    )

    # 학습 결과를 반환
    return response.choices[0].text


# 챗봇 대화 시작
print("챗봇 대화를 시작합니다. 종료하려면 'exit'를 입력하세요.")
while True:
    user_input = input("사용자: ")
    if user_input == "exit":
        break

    # 사용자 입력과 학습된 모델을 이용해 챗봇이 응답
    response = train_gpt2(chat_data + [{"user": user_input, "ai": ""}])
    print("챗봇: " + response.strip())