import streamlit as st

st.title("🎈 2025 음악")
st.info("반갑습니다")
st.write("저는 송내고등학교 음악쌤 입니다")
# 페이지 구조용 제목 출력
st.title("피아노 코드")
st.header("다장조에서 자주 쓰는 코드 진행")
st.subheader("구성음 3개를 모두 말해주세요!")
st.image("https://img.freepik.com/premium-vector/piano-key-keyboard-melody-instrument_250246-301.jpg")
st.snow
# 한 줄 텍스트 입력
name = st.text_input("이름을 입력하세요")
st.write("입력된 이름:", name)

# 여러 줄 텍스트 입력
feedback = st.text_area("의견을 입력하세요")
st.write("입력된 의견:", feedback)