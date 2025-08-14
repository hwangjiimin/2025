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

# MBTI별 특징 데이터
mbti_traits = {
    "INTJ": "📚 전략적 사고와 계획 수립 능력이 뛰어나며, 장기적인 목표를 설정하고 달성하는 데 강점이 있습니다.",
    "INTP": "🧩 호기심이 많고 창의적인 문제 해결 능력을 가진 탐구형 인재입니다.",
    "ENTJ": "🏆 강력한 리더십과 추진력을 가지고 목표를 향해 팀을 이끄는 성향이 강합니다.",
    "ENTP": "💡 새로운 아이디어를 빠르게 만들어내고 변화를 즐기는 혁신가입니다.",
    "INFJ": "🌸 깊은 통찰력과 공감 능력을 바탕으로 타인을 돕는 데 열정적입니다.",
    "INFP": "💖 가치 중심적이며 이상주의적 성향으로 자신이 믿는 바를 위해 노력합니다.",
    "ENFJ": "🤝 사람들을 이끌고 협력하게 만드는 천부적인 리더이자 조력자입니다.",
    "ENFP": "🎆 에너지가 넘치고 창의적이며 사람들과의 관계에서 영감을 주고받습니다.",
    "ISTJ": "📏 체계적이고 신뢰할 수 있으며 책임감 있는 업무 수행 능력이 뛰어납니다.",
    "ISFJ": "🌼 헌신적이고 세심하며 다른 사람을 도와주는 것을 좋아합니다.",
    "ESTJ": "📊 현실적이고 실용적인 접근을 통해 효율적으로 목표를 달성합니다.",
    "ESFJ": "💐 사교적이고 배려심이 깊으며 타인의 필요를 잘 파악합니다.",
    "ISTP": "🛠 실용적이고 문제 해결 능력이 뛰어나며 손으로 무언가를 만드는 것을 즐깁니다.",
    "ISFP": "🎨 예술적 감각이 뛰어나며 감정 표현이 풍부합니다.",
    "ESTP": "🔥 활동적이고 모험을 즐기며 상황에 빠르게 적응합니다.",
    "ESFP": "🎭 사교적이고 유쾌하며 사람들을 즐겁게 만드는 재주가 있습니다."
}

# 페이지 설정
st.set_page_config(page_title="MBTI 직업 추천 🎯", page_icon="🌟", layout="centered")

# 스타일
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
    .trait-card {
        background: #fff0f5;
        padding: 20px;
        margin: 15px 0;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        font-size: 18px;
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
st.write("🔮 MBTI를 선택하면 **추천 직업 + 해당 유형의 특징**을 알려드려요! 💡")

# MBTI 선택
selected_mbti = st.selectbox(
    "당신의 MBTI는 무엇인가요? 😎",
    options=list(mbti_jobs.keys())
)

# 결과 출력
if selected_mbti:
    st.markdown(f"<div class='trait-card'>{mbti_traits[selected_mbti]}</div>", unsafe_allow_html=True)
    st.subheader(f"💎 {selected_mbti} 유형의 추천 직업 🌟")
    for job in mbti_jobs[selected_mbti]:
        st.markdown(f"<div class='job-card'>{job}</div>", unsafe_allow_html=True)
