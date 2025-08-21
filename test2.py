import streamlit as st
import time
import random

# 웹페이지 기본 설정
st.set_page_config(page_title="뽀모도로 타이머 ⏳", page_icon="🍅", layout="centered")

st.title("🍅 뽀모도로 공부 타이머")
st.write("집중 ⏰ → 휴식 ☕ → 다시 집중! 반복하며 효율적으로 공부하세요.")

# 동기부여 명언 리스트
quotes = [
    "성공은 작은 노력이 반복될 때 찾아온다. – 로버트 콜리어",
    "노력하는 자에게 불가능은 없다. – 알렉산더 대왕",
    "포기하지 말라. 지금이 바로 시작할 시간이다. – 노먼 빈센트 필",
    "위대한 일은 열정을 잃지 않고 계속 나아가는 사람에게 찾아온다. – 윈스턴 처칠",
    "오늘 걷지 않으면 내일은 뛰어야 한다. – 이소룡",
    "천재는 노력하는 사람을 이길 수 없고, 노력하는 사람은 즐기는 사람을 이길 수 없다. – 공자",
    "작은 기회로부터 종종 위대한 업적이 시작된다. – 데모스테네스",
    "노력은 배신하지 않는다. – 일본 속담",
    "오늘 할 수 있는 일을 내일로 미루지 마라. – 벤자민 프랭클린",
    "실패는 성공의 어머니이다. – 속담",
    "꾸준함은 천재를 이긴다. – 속담",
    "시작이 반이다. – 아리스토텔레스",
    "꿈은 이루어지기 전까지는 항상 불가능해 보인다. – 넬슨 만델라",
    "천리 길도 한 걸음부터 시작된다. – 노자",
    "포기하지 않으면 아직 끝난 게 아니다. – 마이클 조던",
    "지식에 대한 투자는 최고의 이자율을 낸다. – 벤자민 프랭클린",
    "성공은 준비된 자에게 온다. – 루이 파스퇴르",
    "가장 큰 위험은 위험을 감수하지 않는 것이다. – 마크 저커버그",
    "성공은 행복의 열쇠가 아니라, 행복이 성공의 열쇠다. – 알베르트 슈바이처",
    "작은 습관이 큰 차이를 만든다. – 제임스 클리어",
]

# 세션 상태 초기화
if "running" not in st.session_state:
    st.session_state.running = False
if "total_focus" not in st.session_state:
    st.session_state.total_focus = 0
if "total_break" not in st.session_state:
    st.session_state.total_break = 0
if "total_cycles" not in st.session_state:
    st.session_state.total_cycles = 0

# 타이머 함수
def run_timer(total_seconds, phase_name, color="🔴"):
    progress_bar = st.progress(0)
    status_text = st.empty()
    for i in range(total_seconds):
        mins, secs = divmod(total_seconds - i, 60)
        timer_text = f"{color} {phase_name} 중: {mins:02d}:{secs:02d}"
        status_text.markdown(f"### {timer_text}")
        progress_bar.progress((i + 1) / total_seconds)
        time.sleep(1)

# 실행 중이 아닐 때만 입력창 보이기
if not st.session_state.running:
    focus_minutes = st.number_input("집중 시간 (분)", min_value=1, max_value=120, value=25, step=1)
    break_minutes = st.number_input("휴식 시간 (분)", min_value=1, max_value=60, value=5, step=1)
    cycles = st.number_input("반복 횟수 (사이클 수)", min_value=1, max_value=10, value=4, step=1)

    if st.button("🚀 뽀모도로 시작하기"):
        st.session_state.running = True
        st.session_state.focus_minutes = focus_minutes
        st.session_state.break_minutes = break_minutes
        st.session_state.cycles = cycles
        st.rerun()  # 화면 갱신해서 입력창 숨김

# 실행 중일 때
else:
    for cycle in range(1, st.session_state.cycles + 1):
        st.info(f"💡 {cycle}번째 사이클 명언: *{random.choice(quotes)}*")

        st.success(f"✅ {cycle}번째 집중 시간 시작!")
        run_timer(int(st.session_state.focus_minutes * 60), "집중", "🔥")
        st.session_state.total_focus += st.session_state.focus_minutes

        st.warning("☕ 휴식 시간 시작!")
        run_timer(int(st.session_state.break_minutes * 60), "휴식", "💤")
        st.session_state.total_break += st.session_state.break_minutes

        st.session_state.total_cycles += 1

    st.balloons()
    st.success("🎉 모든 뽀모도로 사이클이 끝났습니다! 고생하셨어요 💪")
    st.session_state.running = False  # 다시 설정 가능하도록 초기화

# 통계 표시
st.subheader("📊 공부 시간 통계")
st.write(f"총 집중 시간: **{st.session_state.total_focus} 분**")
st.write(f"총 휴식 시간: **{st.session_state.total_break} 분**")
st.write(f"완료한 사이클 수: **{st.session_state.total_cycles} 회**")
