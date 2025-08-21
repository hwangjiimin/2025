import streamlit as st
import time
import random
import datetime

# -----------------------------
# 페이지 기본 설정
# -----------------------------
st.set_page_config(page_title="뽀모도로 타이머 ⏳", page_icon="🍅", layout="centered")
st.title("🍅 뽀모도로 공부 타이머")
st.write("집중 ⏰ → 휴식 ☕ → 다시 집중! 반복하며 효율적으로 공부하세요.")

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
# 배경 선택 UI
# -----------------------------
st.sidebar.subheader("🎨 배경 테마 선택")
bg_theme = st.sidebar.selectbox("원하는 배경을 선택하세요", ["기본", "숲속", "바다", "밤하늘", "산"])

bg_images = {
    "숲속": "https://images.unsplash.com/photo-1506765515384-028b60a970df?auto=format&fit=crop&w=1350&q=80",
    "바다": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=1350&q=80",
    "밤하늘": "https://images.unsplash.com/photo-1503264116251-35a269479413?auto=format&fit=crop&w=1350&q=80",
    "산": "https://images.unsplash.com/photo-1501785888041-af3ef285b470?auto=format&fit=crop&w=1350&q=80",
}

if bg_theme != "기본":
    set_background(bg_images[bg_theme])

# -----------------------------
# 자연 소리 선택
# -----------------------------
st.sidebar.subheader("🎵 자연의 소리 선택")
sound_option = st.sidebar.selectbox("백색소음 선택", ["없음", "빗소리", "숲소리", "파도소리"])

sound_urls = {
    "빗소리": "https://www.fesliyanstudios.com/play-mp3/387",
    "숲소리": "https://www.fesliyanstudios.com/play-mp3/671",
    "파도소리": "https://www.fesliyanstudios.com/play-mp3/673",
}

if sound_option != "없음":
    st.sidebar.audio(sound_urls[sound_option])

# -----------------------------
# 동기부여 명언
# -----------------------------
quotes = [
    "성공은 작은 노력이 반복될 때 찾아온다. – 로버트 콜리어",
    "노력하는 자에게 불가능은 없다. – 알렉산더 대왕",
    "포기하지 말라. 지금이 바로 시작할 시간이다. – 노먼 빈센트 필",
    "위대한 일은 열정을 잃지 않고 계속 나아가는 사람에게 찾아온다. – 윈스턴 처칠",
    "오늘 걷지 않으면 내일은 뛰어야 한다. – 이소룡",
    "작은 기회로부터 종종 위대한 업적이 시작된다. – 데모스테네스",
    "천리 길도 한 걸음부터 시작된다. – 노자",
    "포기하지 않으면 아직 끝난 게 아니다. – 마이클 조던",
    "작은 습관이 큰 차이를 만든다. – 제임스 클리어",
]

# -----------------------------
# 세션 상태 초기화
# -----------------------------
if "running" not in st.session_state:
    st.session_state.running = False
if "stop_timer" not in st.session_state:
    st.session_state.stop_timer = False
if "total_focus" not in st.session_state:
    st.session_state.total_focus = 0
if "total_break" not in st.session_state:
    st.session_state.total_break = 0
if "total_cycles" not in st.session_state:
    st.session_state.total_cycles = 0


# -----------------------------
# 사용자 입력
# -----------------------------
if not st.session_state.running:
    focus_minutes = st.number_input("집중 시간 (분)", min_value=1, max_value=120, value=25, step=1)
    break_minutes = st.number_input("휴식 시간 (분)", min_value=1, max_value=60, value=5, step=1)
    cycles = st.number_input("반복 횟수 (사이클 수)", min_value=1, max_value=10, value=4, step=1)

    if st.button("🚀 뽀모도로 시작하기"):
        st.session_state.running = True
        st.session_state.stop_timer = False
        st.session_state.focus_minutes = focus_minutes
        st.session_state.break_minutes = break_minutes
        st.session_state.cycles = cycles
        st.rerun()


    
    if not st.session_state.stop_timer:
        for cycle in range(1, st.session_state.cycles + 1):
            if st.session_state.stop_timer:
                break
            st.info(f"💡 *{random.choice(quotes)}*")
            st.markdown(f"## 🔁 {cycle}/{st.session_state.cycles} 번째 사이클")

            run_timer(int(st.session_state.focus_minutes * 60), "집중", "🔥")
            if st.session_state.stop_timer:
                break
            st.session_state.total_focus += st.session_state.focus_minutes

            run_timer(int(st.session_state.break_minutes * 60), "휴식", "💤")
            if st.session_state.stop_timer:
                break
            st.session_state.total_break += st.session_state.break_minutes

            st.session_state.total_cycles += 1

        if not st.session_state.stop_timer:
            st.balloons()
            st.success("🎉 모든 뽀모도로 사이클이 끝났습니다! 고생하셨어요 💪")
        st.session_state.running = False

# -----------------------------
# 통계 표시
# -----------------------------
st.subheader("📊 공부 시간 통계")
st.write(f"총 집중 시간: **{st.session_state.total_focus} 분**")
st.write(f"총 휴식 시간: **{st.session_state.total_break} 분**")
st.write(f"완료한 사이클 수: **{st.session_state.total_cycles} 회**")
