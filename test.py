import streamlit as st
import time
import random

st.set_page_config(page_title="Pomodoro Timer", page_icon="⏳", layout="centered")

# --- 세션 상태 초기화 ---
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
if "stop_requested" not in st.session_state:
    st.session_state.stop_requested = False

# --- 명언 모음 ---
quotes = [
    "성공은 작은 노력이 반복된 결과다. – 로버트 콜리어",
    "오늘 할 수 있는 일을 내일로 미루지 마라. – 벤자민 프랭클린",
    "포기하지 않는 사람이 결국 승리한다. – 나폴레온",
    "위대한 일은 열정을 가지고 해야 한다. – 헤겔",
    "작은 습관이 큰 변화를 만든다. – 제임스 클리어",
    "성공의 비밀은 꾸준함에 있다. – 아리스토텔레스",
    "천재는 1%의 영감과 99%의 노력이다. – 토마스 에디슨",
    "할 수 있다고 믿으면 이미 반은 이룬 것이다. – 시어도어 루스벨트",
    "노력하는 사람에게 불가능은 없다. – 알렉산더 대왕",
    "실패는 성공의 어머니이다. – 속담"
]

# --- 타이머 함수 ---
def pomodoro_timer(minutes, phase):
    seconds = minutes * 60
    start_time = time.time()
    while seconds > 0:
        if st.session_state.stop_requested:  # 정지 요청 시 종료
            st.session_state.stop_requested = False
            st.session_state.running = False
            st.warning("⏹ 사이클이 중지되었습니다.")
            return False
        mins, secs = divmod(seconds, 60)
        timer_display = f"{mins:02d}:{secs:02d}"
        st.metric(f"{phase} 남은 시간", timer_display)
        time.sleep(1)
        seconds -= 1
    return True

# --- UI ---
st.title("⏳ 뽀모도로 공부 타이머")

if not st.session_state.running:
    st.subheader("공부/휴식 시간을 설정하세요")
    st.session_state.focus_time = st.number_input("공부 시간 (분)", min_value=1, max_value=120, value=25)
    st.session_state.break_time = st.number_input("휴식 시간 (분)", min_value=1, max_value=60, value=5)

    if st.button("▶ 시작하기"):
        st.session_state.running = True
        st.session_state.cycle += 1
        st.session_state.stop_requested = False
else:
    # 정지 버튼
    if st.button("⏹ 정지하기"):
        st.session_state.stop_requested = True

    # 명언 표시 (사이클마다 다르게)
    st.info(f"💡{random.choice(quotes)}")

    # --- 사이클 실행 ---
    with st.spinner("공부 사이클 진행 중..."):
        if pomodoro_timer(st.session_state.focus_time, "공부"):
            st.success("공부 완료! 잠깐 휴식을 취하세요. 🌿")
            st.session_state.stats.append(("공부", st.session_state.focus_time))

        if not st.session_state.stop_requested:  # 정지 안했으면 휴식 실행
            if pomodoro_timer(st.session_state.break_time, "휴식"):
                st.success("휴식 완료! 다시 집중할 시간입니다. 🚀")
                st.session_state.stats.append(("휴식", st.session_state.break_time))

    st.session_state.running = False  # 사이클 종료 후 다시 설정창 보이게

# --- 통계 ---
st.subheader("📊 공부 시간 통계")
if st.session_state.stats:
    total_focus = sum(t for phase, t in st.session_state.stats if phase == "공부")
    st.write(f"총 공부한 시간: **{total_focus}분**")
    st.write(st.session_state.stats)
else:
    st.write("아직 기록이 없습니다.")

