import os
import openai
openai.api_key = "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"  # OpenAI API key 설정

prompt = "Hello, what is your name?"  # 입력으로 사용될 프롬프트
temperature = 0.7  # 다양성 조절을 위한 옵션. 기본값은 0.5입니다.

# API를 통해 입력된 프롬프트를 이용해 다음 단어를 예측합니다.
response = openai.Completion.create(
    engine="davinci",  # 사용할 모델의 엔진을 설정합니다.
    prompt=prompt,
    temperature=temperature,
    max_tokens=60,  # 출력할 최대 단어 수를 설정합니다.
    n=1,  # 출력할 결과의 수를 설정합니다.
    stop=None,  # 출력 결과의 종료 조건을 설정합니다. None으로 설정할 경우 자동 종료됩니다.
)

# API로부터 받은 응답 중 첫 번째 결과를 출력합니다.
print(response.choices[0].text)




