import streamlit as st
import time
import random

# --- 명언 리스트 ---
QUOTES = [
    "성공은 작은 노력이 반복될 때 나타난다.",
    "오늘의 노력은 내일의 자산이다.",
    "지금의 고통은 미래의 힘이다.",
    "작은 습관이 큰 변화를 만든다.",
    "포기하지 않는 자가 결국 이긴다.",
    "한 걸음 한 걸음이 모여 큰 길이 된다.",
    "오늘 할 일을 내일로 미루지 마라.",
    "끝까지 해내는 자가 진정한 승자다."
]

# --- 세션 상태 초기화 ---
if "running" not in st.session_state:
    st.session_state.running = False
if "cycle" not in st.session_state:
    st.session_state.cycle = 0
if "focus_time" not in st.session_state:
    st.session_state.focus_time = 25
if "break_time" not in st.session_state:
    st.session_state.break_time = 5
if "remaining_focus" not in st.session_state:
    st.session_state.remaining_focus = st.session_state.focus_time * 60
if "remaining_break" not in st.session_state:
    st.session_state.remaining_break = st.session_state.break_time * 60
if "in_focus_phase" not in st.session_state:
    st.session_state.in_focus_phase = True
if "stats" not in st.session_state:
    st.session_state.stats = []

# --- UI ---
st.title("⏳ 이어서 실행 가능한 뽀모도로 타이머")
st.write("정지 후에도 이어서 진행 가능합니다. 🔄")

# 입력창 (실행 중이 아닐 때만 보이게)
if not st.session_state.running and st.session_state.remaining_focus == st.session_state.focus_time * 60:
    st.session_state.focus_time = st.number_input("집중 시간 (분)", 1, 120, st.session_state.focus_time)
    st.session_state.break_time = st.number_input("휴식 시간 (분)", 1, 60, st.session_state.break_time)
    st.session_state.remaining_focus = st.session_state.focus_time * 60
    st.session_state.remaining_break = st.session_state.break_time * 60

if st.button("▶ 시작/이어하기"):
    st.session_state.running = True

if st.button("⏹ 정지"):
    st.session_state.running = False

# --- 타이머 표시 영역 ---
timer_placeholder = st.empty()
quote_placeholder = st.empty()

# --- 타이머 함수 ---
def run_timer(remaining_seconds, label):
    start_time = time.time()
    end_time = start_time + remaining_seconds
    while time.time() < end_time and st.session_state.running:
        remaining = int(end_time - time.time())
        mins, secs = divmod(remaining, 60)
        timer_placeholder.markdown(f"### ⏰ {label} 남은 시간: **{mins:02d}:{secs:02d}**")
        time.sleep(1)
    return remaining if st.session_state.running else int(end_time - time.time())

# --- 사이클 실행 ---
if st.session_state.running:
    # 명언 표시 (한 번만)
    quote_placeholder.markdown(f"💡 오늘의 명언: *{random.choice(QUOTES)}*")

    if st.session_state.in_focus_phase:
        st.session_state.remaining_focus = run_timer(st.session_state.remaining_focus, "집중")
        if st.session_state.remaining_focus <= 0:
            st.success("✅ 집중 완료! 휴식 시간입니다.")
            st.session_state.stats.append(("집중", st.session_state.focus_time))
            st.session_state.in_focus_phase = False
            st.session_state.remaining_break = st.session_state.break_time * 60
    else:
        st.session_state.remaining_break = run_timer(st.session_state.remaining_break, "휴식")
        if st.session_state.remaining_break <= 0:
            st.success("☕ 휴식 완료! 다시 집중 시작!")
            st.session_state.stats.append(("휴식", st.session_state.break_time))
            st.session_state.in_focus_phase = True
            st.session_state.remaining_focus = st.session_state.focus_time * 60
            st.session_state.cycle += 1

# --- 통계 표시 ---
st.subheader("📊 공부 통계")
if st.session_state.stats:
    total_focus = sum(t for phase, t in st.session_state.stats if phase == "집중")
    total_break = sum(t for phase, t in st.session_state.stats if phase == "휴식")
    st.write(f"총 집중 시간: **{total_focus}분**")
    st.write(f"총 휴식 시간: **{total_break}분**")
    st.write(f"완료한 사이클 수: **{st.session_state.cycle}회**")
else:
    st.write("아직 기록이 없습니다.")
