import streamlit as st
import random

# -----------------------------
# 페이지 기본 설정
# -----------------------------
st.set_page_config(page_title="뽀모도로 감성공간 🍃", page_icon="🍅", layout="centered")
st.title("🍅 뽀모도로 공부 공간")
st.write("당신의 집중을 돕기 위한 감성적 공간입니다. 🎧")

# -----------------------------
# 배경 설정 함수
# -----------------------------
def set_background(image_url):
    css = f"""
    <style>
    [data-testid="stAppViewContainer"] {{
        background-image: url('{image_url}');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    [data-testid="stHeader"], [data-testid="stToolbar"] {{
        background: rgba(255,255,255,0);
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

# -----------------------------
# 배경 선택
# -----------------------------
st.sidebar.subheader("🎨 배경 테마 선택")
bg_theme = st.sidebar.selectbox("배경을 선택하세요", ["기본", "숲속", "바다", "밤하늘", "산"])

bg_images = {
    "숲속": "https://images.unsplash.com/photo-1506765515384-028b60a970df?auto=format&fit=crop&w=1350&q=80",
    "바다": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=1350&q=80",
    "밤하늘": "https://images.unsplash.com/photo-1503264116251-35a269479413?auto=format&fit=crop&w=1350&q=80",
    "산": "https://images.unsplash.com/photo-1501785888041-af3ef285b470?auto=format&fit=crop&w=1350&q=80",
}

if bg_theme != "기본":
    set_background(bg_images[bg_theme])

# -----------------------------
# 자연의 소리
# -----------------------------
st.sidebar.subheader("🎵 자연의 소리 선택")
sound_option = st.sidebar.selectbox("백색소음 재생", ["없음", "빗소리", "숲소리", "파도소리"])

sound_urls = {
    "빗소리": "https://www.fesliyanstudios.com/play-mp3/387",
    "숲소리": "https://www.fesliyanstudios.com/play-mp3/671",
    "파도소리": "https://www.fesliyanstudios.com/play-mp3/673",
}

if sound_option != "없음":
    st.audio(sound_urls[sound_option])

# -----------------------------
# 동기부여 명언
# -----------------------------
quotes = [
    "성공은 작은 노력이 반복될 때 찾아온다. – 로버트 콜리어",
    "노력하는 자에게 불가능은 없다. – 알렉산더 대왕",
    "오늘 걷지 않으면 내일은 뛰어야 한다. – 이소룡",
    "작은 기회로부터 종종 위대한 업적이 시작된다. – 데모스테네스",
    "천리 길도 한 걸음부터 시작된다. – 노자",
    "포기하지 않으면 아직 끝난 게 아니다. – 마이클 조던",
    "작은 습관이 큰 차이를 만든다. – 제임스 클리어",
]

if st.button("💡 동기부여 명언 보기"):
    st.success(f"💬 {random.choice(quotes)}")

# -----------------------------
# 수동 학습 통계 입력
# -----------------------------
st.subheader("📊 오늘의 공부 기록")
focus_input = st.number_input("오늘 집중한 시간 (분)", min_value=0, value=0, step=1)
break_input = st.number_input("오늘 휴식한 시간 (분)", min_value=0, value=0, step=1)

if st.button("✅ 기록 반영하기"):
    total = focus_input + break_input
    st.info(f"✨ 총 공부 관련 시간은 **{total}분**입니다. 고생하셨어요!")

# -----------------------------
# 감성 문구
# -----------------------------
st.markdown("---")
st.markdown("🌿 오늘도 한 걸음 더 나아간 당신을 응원합니다.")
