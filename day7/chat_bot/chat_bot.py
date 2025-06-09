import streamlit as st
import ollama

# 상태를 관리하는 함수
def init_session_state(key : dict) :
    pass

# 메세지를 받아 딕셔너리로 만들어주는 함수?
def chat_message_user(prompt : str) -> dict : 
    pass

# 모델이 답변하는 걸 관리하는 함수
def chat_message_llm(role : str, model : str, message : list) -> dict :
    pass

# 파이썬 인터프리터에 들어가 실행이 되면 __name__ 에 __main__ 을 넣어줌
# 실행 파일인지 확인하기 위한 코드
if __name__ == '__main__' :
    st.set_page_config(layout = 'wide')
    st.title('🤯제발 그만좀... 물어보면 안되겠니?')

    init_session_state(dict(msgs = [])) # {[]}
    msgs = st.session_state['msgs']
    