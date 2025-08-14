import streamlit as st

# MBTI별 추천 직업 데이터
mbti_jobs = {
    "INTJ": ["전략 컨설턴트", "연구원", "데이터 과학자"],
    "INTP": ["프로그래머", "발명가", "연구원"],
    "ENTJ": ["기업가", "프로젝트 매니저", "경영 컨설턴트"],
    "ENTP": ["마케팅 디렉터", "창업가", "벤처 투자자"],
    "INFJ": ["작가", "심리상담사", "교육 컨설턴트"],
    "INFP": ["예술가", "작곡가", "작가"],
    "ENFJ": ["교사", "인사담당자", "교육 지도자"],
    "ENFP": ["홍보 담당자", "방송 작가", "광고 기획자"],
    "ISTJ": ["회계사", "법률 전문가", "행정 공무원"],
    "ISFJ": ["간호사", "사회복지사", "교사"],
    "ESTJ": ["경영자", "군인", "프로젝트 매니저"],
    "ESFJ": ["영업 관리자", "이벤트 플래너", "교사"],
    "ISTP": ["기계 엔지니어", "파일럿", "응급 구조사"],
    "ISFP": ["디자이너", "사진작가", "작곡가"],
    "ESTP": ["세일즈 전문가", "스포츠 코치", "기업가"],
    "ESFP": ["배우", "이벤트 기획자", "방송인"]
}

st.set_page_config(page_title="MBTI 직업 추천", page_icon="🎯", layout="centered")

# 제목
st.title("🎯 MBTI 기반 진로 추천 사이트")
st.write("MBTI를 선택하면 해당 유형에 맞는 직업을 추천해 드립니다.")

# 사용자 입력
selected_mbti = st.selectbox(
    "당신의 MBTI를 선택하세요:",
    options=list(mbti_jobs.keys())
)

# 결과 출력
if selected_mbti:
    st.subheader(f"💡 {selected_mbti} 유형의 추천 직업")
    for job in mbti_jobs[selected_mbti]:
        st.write(f"- {job}")

# 추가 기능 - 설명
if st.checkbox("MBTI 유형별 특징 보기"):
    st.info(f"{selected_mbti} 유형은 분석적 사고, 성실함, 창의성 등 다양한 강점을 가지고 있습니다. "
            f"따라서 위 직업들이 적합할 수 있습니다.")
