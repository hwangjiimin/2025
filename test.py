import streamlit as st
import random

# -----------------------------
# 웹페이지 기본 설정
# -----------------------------
st.set_page_config(page_title="뽀모도로 타이머 ⏳", page_icon="🍅", layout="centered")
st.title("🍅 뽀모도로 공부 타이머")
st.write("집중 ⏰ → 휴식 ☕ → 다시 집중! 반복하며 효율적으로 공부하세요.")

# -----------------------------
# 동기부여 명언 리스트
# -----------------------------
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

# -----------------------------
# 세션 상태 초기화
# -----------------------------
if "total_focus" not in st.session_state:
    st.session_state.total_focus = 0
if "total_break" not in st.session_state:
    st.session_state.total_break = 0
if "total_cycles" not in st.session_state:
    st.session_state.total_cycles = 0

# -----------------------------
# 사용자 수동 입력
# -----------------------------
st.subheader("📝 오늘의 뽀모도로 기록하기")

focus_input = st.number_input("집중 시간 (분)", min_value=0, value=0, step=1)
break_input = st.number_input("휴식 시간 (분)", min_value=0, value=0, step=1)
cycles_input = st.number_input("완료한 사이클 수", min_value=0, value=0, step=1)

if st.button("✅ 기록 반영"):
    st.session_state.total_focus += focus_input
    st.session_state.total_break += break_input
    st.session_state.total_cycles += cycles_input
    st.success("📌 오늘의 기록이 반영되었습니다!")

# -----------------------------
# 동기부여 메시지
# -----------------------------
if st.button("💬 동기부여 명언 보기"):
    st.info(random.choice(quotes))

# -----------------------------
# 통계 표시
# -----------------------------
st.subheader("📊 누적 공부 통계")
st.write(f"총 집중 시간: **{st.session_state.total_focus} 분**")
st.write(f"총 휴식 시간: **{st.session_state.total_break} 분**")
st.write(f"완료한 사이클 수: **{st.session_state.total_cycles} 회**")
st.write(f"총 공부 관련 시간: **{st.session_state.total_focus + st.session_state.total_break} 분**")

# -----------------------------
# 감성 마무리
# -----------------------------
st.markdown("---")
st.markdown("🌿 오늘도 집중한 당신, 멋져요. 계속해서 꾸준히 나아가요!")
