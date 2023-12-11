"""
# My first app
Here's our first attempt at using data to create a table:
"""

import streamlit as st

# Streamlit 애플리케이션 제목
st.title("문자열 검사 애플리케이션")

# 텍스트 입력 필드
user_input = st.text_input("문자열을 입력하세요", "Hello, Streamlit!")

# 입력된 문자열 검사 및 결과 출력
if st.button("검사"):
    reversed_string = user_input[::-1]
    st.write(f"입력된 문자열: {user_input}")
    st.write(f"뒤집힌 문자열: {reversed_string}")
