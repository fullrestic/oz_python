import ollama

# 질문 1
# role과 content로 구성하는 것이 일반적인 rule임
msg = [{'role' : 'user', 'content' : '내 이름은 주현이야! 답변은 한글로 해줘!'}]

# chat 기능을 쓸때 정해줘야 할 것 : model 필수, 나머지는 생략 가능(기본값 None으로 들어감)
# 변수는 이미 정해져 있고, 원하는 값을 넣어야 제대로 작동
# 전달해주면 올라마가 받아서 응답을 return해줌
response_1 =ollama.chat(
    model = 'gemma2:9b',
    messages = msg
)

# 여러 정보 중 메세지-컨텐트 출력
print(response_1['message']['content'])

msg.append(response_1['message'])
# msg = [{'role' : 'user', 'content' : '내 이름은 주현이야! 답변은 한글로 해줘!'}, {'role' : 'assostamt', 'content' : '안녕하세요, 주현님! 반가워요 😊  \n\n저는 한국어로 대화할 수 있는 AI입니다. 무엇을 도와드릴까요? 😄  \n'}]

# 질문 2
msg.append({'role' : 'user', 'content' : '내 이름이 뭐라고?'})

response_2 =ollama.chat(
    model = 'gemma2:9b',
    messages = msg
)

msg.append(response_2['message'])
print(msg)