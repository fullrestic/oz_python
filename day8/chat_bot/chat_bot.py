import streamlit as st
import ollama

# session_state 초기화 함수
def init_session_state(keys : dict) :
    for key, value in keys.items() :    # key -> msgs / val -> []
        if key not in st.session_state :
            st.session_state[key] = value   # st.session_state[msgs] = []

# 메세지를 받아 딕셔너리로 만들어주는 함수?
def chat_message_user(prompt : str) -> dict : 
    with st.chat_message('user') :
        st.markdown(prompt) # markdown : 마크다운 형식으로 변경시켜줌, print문과 비슷하다고 생각하면 됨
    return dict(role = 'user', content = prompt)

# 입력한 내용을 올라마에 전달하고 올라마의 답변을 받아오는 함수
def chat_message_llm(role : str, model : str, messages : list) -> dict :
    with st.chat_message(role) :
        with st.spinner('답변을 준비중입니다.') : # spinner는 로딩중에 보여줄 것을 보여줌
            print(role, model, messages)
            response = ollama.chat(model = model, messages = messages)
            msg_llm = response.get('message', {})   # message만 가져오고, message가 없으면 빈 딕셔너리를 가져옴
            st.markdown(msg_llm['content'])
    return msg_llm

# 파이썬 인터프리터에 들어가 실행이 되면 __name__ 에 __main__ 을 넣어줌
# 실행 파일인지 확인하기 위한 코드
if __name__ == '__main__' :
    st.set_page_config(layout = 'wide')
    st.title('🤯제발 그만좀... 물어보면 안되겠니?')

    init_session_state(dict(msgs = [])) # {msgs : []}
    msgs = st.session_state['msgs']

    for row in msgs : 
        with st.chat_message(row['role']) :
            st.markdown(row['content']) 

    # 프롬프트 창에 입력한 문자열이 prompt로 들어감
    if prompt := st.chat_input('여기에 대화를 입력하세요') :
        msg_user = chat_message_user(prompt)    # dict(role = 'user', content = prompt)
        msgs.append(msg_user)   # [{'user' : '안녕}]

        msg_llm = chat_message_llm('assistant', 'gemma2:9b', msgs)  # response.get('message', {})
        msgs.append(msg_llm)
        