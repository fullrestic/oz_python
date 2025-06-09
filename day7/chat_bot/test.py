import streamlit as st

with st.chat_message("user") :
    st.write("Hello 👋🏻")

# 채팅 입력받는 기능 활성화
prompt = st.chat_input("궁금한 게 있으면 물어봐")  
