import streamlit as st
import time
import random

# 명언 리스트
QUOTES = [
    "성공은 작은 노력이 반복될 때 찾아온다.",
    "오늘의 노력은 내일의 자산이다.",
    "지금의 고통은 미래의 힘이다.",
    "작은 습관이 큰 변화를 만든다.",
    "포기하지 않는 자가 결국 이긴다.",
    "한 걸음 한 걸음이 모여 큰 길이 된다.",
    "오늘 할 일을 내일로 미루지 마라.",
    "끝까지 해내는 자가 진정한 승자다."
]

# 세션 상태 초기화
if "running" not in st.session_state:
    st.session_state.running = False
if "cycle" not in st.session_state:
    st.session_state.cycle = 0
if "focus_time" not in st.session_state:
    st.session_state.focus_time = 25
if "break_time" not in st.session_state:
    st.session_state.break_time = 5
if "stats" not in st.session_state:
    st.session_state.stats = []

st.title("⏳ 뽀모도로 공부 타이머")
st.write("사이클마다 새로운 명언이 나타납니다! ✨")

# 타이머 실행 중이 아닐 때만 시간 선택 가능
if not st.session_state.running:
    st.session_state.focus_time = st.number_input("집중 시간 (분)", 1, 120, 25)
    st.session_state.break_time = st.number_input("휴식 시간 (분)", 1, 60, 5)
    if st.button("▶ 시작"):
        st.session_state.running = True

# 정지 버튼
if st.session_state.running:
    if st.button("⏹ 정지"):
        st.session_state.running = False

# 타이머 표시 영역
timer_placeholder = st.empty()
quote_placeholder = st.empty()

def run_timer(seconds, label):
    start_time = time.time()
    end_time = start_time + seconds
    while time.time() < end_time and st.session_state.running:
        remaining = int(end_time - time.time())
        mins, secs = divmod(remaining, 60)
        timer_placeholder.markdown(f"### ⏰ {label} 남은 시간: **{mins:02d}:{secs:02d}**")
        time.sleep(1)

# 사이클 실행
if st.session_state.running:
    st.session_state.cycle += 1
    quote = random.choice(QUOTES)
    quote_placeholder.markdown(f"💡 오늘의 명언: *{quote}*")

    # 집중 시간
    run_timer(st.session_state.focus_time * 60, "집중")
    if st.session_state.running:
        st.session_state.stats.append(
            {"cycle": st.session_state.cycle, "focus": st.session_state.focus_time, "break": st.session_state.break_time}
        )
        # 휴식 시간
        run_timer(st.session_state.break_time * 60, "휴식")

# 공부 통계 표시
st.write("📊 공부 통계")
if len(st.session_state.stats) > 0:
    st.table(st.session_state.stats)
else:
    st.write("아직 기록이 없습니다.")


