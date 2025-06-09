import streamlit as st

# session_state : 상태 정보를 알려주는 기능
# 상태 정보에 카운트 정보가 없으면 0으로 초기화
if 'count' not in st.session_state :
    st.session_state.count = 0

# 버튼 생성
increment = st.button('1원씩 증가하는 버튼')

if increment : 
    st.session_state.count += 1
    
st.write('count = ', st.session_state.count)
