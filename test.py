import streamlit as st
import time

# 웹페이지 기본 설정
st.set_page_config(page_title="공부 타이머 ⏳", page_icon="📚", layout="centered")

st.title("📚 공부 타이머")
st.write("⏳ 원하는 시간을 설정하고 집중 모드로 들어가 보세요!")

# 사용자 입력 (분 단위)
minutes = st.number_input("공부할 시간을 분 단위로 입력하세요:", min_value=1, max_value=120, value=25, step=1)

# 시작 버튼
if st.button("🚀 타이머 시작하기"):
    total_seconds = int(minutes * 60)
    progress_bar = st.progress(0)
    status_text = st.empty()

    for i in range(total_seconds):
        mins, secs = divmod(total_seconds - i, 60)
        timer_text = f"⏰ 남은 시간: {mins:02d}:{secs:02d}"
        status_text.markdown(f"### {timer_text}")
        progress_bar.progress((i + 1) / total_seconds)
        time.sleep(1)

    st.success("🎉 공부 시간이 끝났습니다! 휴식하세요 ☕")
