import streamlit as st
import data.py

def check_consecutive_substring(input_str, consecutive_str_list):
    for pattern in consecutive_str_list:
        count = 0
        for char in input_str:
            if char in pattern:
                count += 1
                if count >= 4:
                    st.write("연속된 문자열 포함됨")
                    return
            else:
                count = 0
        count = 0
    else:
        st.write("연속된 문자열 포함 안됨")


# Streamlit 애플리케이션 제목
st.title("다양한 검사를 수행하는 애플리케이션")

# 텍스트 입력 필드
user_input = st.text_input("문자열을 입력하세요", "Sample sentence to check.")

# 검사 및 결과 출력
if st.button("검사"):
    # word_list 검사
    included_words = [word for word in word_list if word in user_input]
    if included_words:
        st.write(f"입력된 문자열에 다음 단어들이 포함되어 있습니다: {', '.join(included_words)}")
    else:
        st.write("입력된 문자열에는 word_list에 포함된 단어가 포함되어 있지 않습니다.")

    # user_name_list 검사
    included_names = [name for name in user_name_list if name in user_input.lower()]
    if included_names:
        st.write(f"입력된 문자열에 다음 이름들이 포함되어 있습니다: {', '.join(included_names)}")
    else:
        st.write("입력된 문자열에는 user_name_list에 포함된 이름이 포함되어 있지 않습니다.")

    # consecutive_str_list 검사
    check_consecutive_substring(user_input, consequence_list)