import streamlit as st

# session_state : 상태 정보를 알려주는 기능
# 상태 정보에 카운트 정보가 없으면 0으로 초기화
if 'counter' not in st.session_state :
    st.session_state.counter = 0
    # session_state에 들어가는 변수명은 바뀌어도 상관없음. 사용자 지정 변수!

# 버튼 생성
increment = st.button('1원씩 증가하는 버튼')

if increment : 
    st.session_state.counter += 1
    
st.write('counter = ', st.session_state.counter)
