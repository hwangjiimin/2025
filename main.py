import streamlit as st

# MBTI별 추천 직업 데이터
mbti_jobs = {
    "INTJ": ["🧠 전략 컨설턴트", "🔬 연구원", "📊 데이터 과학자"],
    "INTP": ["💻 프로그래머", "💡 발명가", "🔍 연구원"],
    "ENTJ": ["🏢 기업가", "📈 프로젝트 매니저", "📊 경영 컨설턴트"],
    "ENTP": ["📢 마케팅 디렉터", "🚀 창업가", "💰 벤처 투자자"],
    "INFJ": ["✍ 작가", "💬 심리상담사", "📚 교육 컨설턴트"],
    "INFP": ["🎨 예술가", "🎼 작곡가", "📖 작가"],
    "ENFJ": ["👩‍🏫 교사", "🧑‍💼 인사담당자", "📚 교육 지도자"],
    "ENFP": ["📣 홍보 담당자", "📝 방송 작가", "🎯 광고 기획자"],
    "ISTJ": ["📑 회계사", "⚖ 법률 전문가", "🏛 행정 공무원"],
    "ISFJ": ["💉 간호사", "🤝 사회복지사", "👩‍🏫 교사"],
    "ESTJ": ["🏆 경영자", "🪖 군인", "📅 프로젝트 매니저"],
    "ESFJ": ["🤝 영업 관리자", "🎊 이벤트 플래너", "👩‍🏫 교사"],
    "ISTP": ["⚙ 기계 엔지니어", "✈ 파일럿", "🚑 응급 구조사"],
    "ISFP": ["🎨 디자이너", "📷 사진작가", "🎼 작곡가"],
    "ESTP": ["💼 세일즈 전문가", "🏋 스포츠 코치", "🚀 기업가"],
    "ESFP": ["🎭 배우", "🎉 이벤트 기획자", "📺 방송인"]
}

# 페이지 설정
st.set_page_config(page_title="MBTI 직업 추천 🎯", page_icon="🌟", layout="centered")

# 커스텀 스타일 (폰트, 색상, 그림자)
st.markdown("""
    <style>
    body {
        background: linear-gradient(120deg, #f6d365 0%, #fda085 100%);
        font-family: 'Arial', sans-serif;
    }
    .big-title {
        text-align: center;
        font-size: 48px !important;
        color: white;
        text-shadow: 2px 2px 4px #000000;
    }
    .job-card {
        background: white;
        padding: 20px;
        margin: 10px 0;
        border-radius: 15px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.2);
        font-size: 20px;
    }
    .stSelectbox label {
        font-size: 20px;
        font-weight: bold;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# 제목
st.markdown("<h1 class='big-title'>🌈✨ MBTI 직업 추천 💼🎯</h1>", unsafe_allow_html=True)
st.write("🔮 당신의 MBTI를 선택하면 맞춤형 직업 리스트를 알려드려요! 💡")

# MBTI 선택
selected_mbti = st.selectbox(
    "당신의 MBTI는 무엇인가요? 😎",
    options=list(mbti_jobs.keys())
)

# 추천 직업 출력
if selected_mbti:
    st.subheader(f"💎 {selected_mbti} 유형의 추천 직업 🌟")
    for job in mbti_jobs[selected_mbti]:
        st.markdown(f"<div class='job-card'>{job}</div>", unsafe_allow_html=True)

# 유형별 설명 체크박스
if st.checkbox("📜 MBTI 유형별 특징 보기"):
    st.success(f"🌟 {selected_mbti} 유형은 자신만의 강점을 살려 미래를 개척하는 멋진 타입입니다! "
               f"🚀 위 추천 직업들이 당신의 재능과 잘 어울릴 수 있어요. 💖")
