import streamlit as st
import time
import random
from datetime import datetime, timedelta

st.set_page_config(page_title="뽀모도로 공부 타이머", page_icon="⏱️", layout="centered")

# ========================
# 명언 모음
# ========================
quotes = [
    "작은 습관이 큰 변화를 만든다.",
    "오늘의 노력은 내일의 성공으로 이어진다.",
    "포기하지 마라. 위대한 일은 시간이 걸린다.",
    "시작이 반이다.",
    "천 리 길도 한 걸음부터.",
    "노력은 배신하지 않는다.",
    "실패는 성공의 어머니.",
    "성공은 준비된 자에게 온다.",
    "조금 늦어도 괜찮다. 멈추지만 않으면 된다.",
    "오늘의 나는 어제의 나를 이긴 결과다."
]

# ========================
# 상태 초기화
# ========================
if "is_running" not in st.session_state:
    st.session_state.is_running = False
if "is_paused" not in st.session_state:
    st.session_state.is_paused = False
if "phase" not in st.session_state:  # "focus" or "break"
    st.session_state.phase = "focus"
if "end_time" not in st.session_state:
    st.session_state.end_time = None
if "remaining_time" not in st.session_state:
    st.session_state.remaining_time = 0
if "cycle_count" not in st.session_state:
    st.session_state.cycle_count = 0
if "quote" not in st.session_state:
    st.session_state.quote = random.choice(quotes)
if "stats" not in st.session_state:
    st.session_state.stats = []  # (날짜, 집중시간 분)


# ========================
# 함수 정의
# ========================
def start_timer(focus_minutes, break_minutes):
    st.session_state.is_running = True
    st.session_state.is_paused = False
    st.session_state.focus_minutes = focus_minutes
    st.session_state.break_minutes = break_minutes

    # 새로운 타이머 시작
    if st.session_state.phase == "focus":
        st.session_state.remaining_time = focus_minutes * 60
    else:
        st.session_state.remaining_time = break_minutes * 60

    st.session_state.end_time = datetime.now() + timedelta(seconds=st.session_state.remaining_time)


def pause_timer():
    st.session_state.is_paused = True
    if st.session_state.end_time:
        st.session_state.remaining_time = int((st.session_state.end_time - datetime.now()).total_seconds())
    st.session_state.end_time = None


def resume_timer():
    st.session_state.is_paused = False
    st.session_state.end_time = datetime.now() + timedelta(seconds=st.session_state.remaining_time)


def reset_phase():
    # 사이클 종료 시
    if st.session_state.phase == "focus":
        st.session_state.stats.append((datetime.now().date(), st.session_state.focus_minutes))
        st.session_state.phase = "break"
    else:
        st.session_state.phase = "focus"
        st.session_state.cycle_count += 1
        st.session_state.quote = random.choice(quotes)

    # 새로운 사이클 시작
    if st.session_state.phase == "focus":
        st.session_state.remaining_time = st.session_state.focus_minutes * 60
    else:
        st.session_state.remaining_time = st.session_state.break_minutes * 60
    st.session_state.end_time = datetime.now() + timedelta(seconds=st.session_state.remaining_time)


# ========================
# UI
# ========================
st.title("⏱️ 뽀모도로 공부 타이머")
st.write("집중과 휴식을 반복하며 효율적으로 공부하세요!")

# 타이머 설정창 (실행 중일 때는 숨김)
if not st.session_state.is_running:
    focus_minutes = st.number_input("집중 시간 (분)", 1, 120, 25)
    break_minutes = st.number_input("휴식 시간 (분)", 1, 60, 5)

    if st.button("▶️ 시작하기"):
        start_timer(focus_minutes, break_minutes)

else:
    # 현재 상태 보여주기
    phase_name = "집중 시간 🔥" if st.session_state.phase == "focus" else "휴식 시간 🌿"
    st.subheader(f"현재: {phase_name}")

    # 남은 시간 계산
    if st.session_state.end_time and not st.session_state.is_paused:
        st.session_state.remaining_time = int((st.session_state.end_time - datetime.now()).total_seconds())

    if st.session_state.remaining_time <= 0 and not st.session_state.is_paused:
        reset_phase()

    minutes, seconds = divmod(st.session_state.remaining_time, 60)
    st.markdown(f"<h1 style='text-align:center; font-size:60px;'>{minutes:02d}:{seconds:02d}</h1>", unsafe_allow_html=True)

    # 버튼 영역
    col1, col2 = st.columns(2)
    with col1:
        if not st.session_state.is_paused:
            if st.button("⏸ 정지"):
                pause_timer()
        else:
            if st.button("▶️ 다시 시작"):
                resume_timer()
    with col2:
        if st.button("⏹ 초기화"):
            st.session_state.is_running = False
            st.session_state.is_paused = False
            st.session_state.phase = "focus"
            st.session_state.end_time = None
            st.session_state.remaining_time = 0

    # 현재 명언
    st.info(f"💡 오늘의 명언: *{st.session_state.quote}*")

# ========================
# 공부 통계
# ========================
st.markdown("---")
st.subheader("📊 공부 통계")
if st.session_state.stats:
    total_focus = sum([s[1] for s in st.session_state.stats])
    st.write(f"총 집중 시간: **{total_focus}분**")
    st.write("기록:")
    for day, minutes in st.session_state.stats:
        st.write(f"- {day}: {minutes}분 집중")
else:
    st.write("아직 기록이 없습니다.")
