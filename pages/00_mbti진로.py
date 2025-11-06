import streamlit as st

# Simple Streamlit app that recommends 2 careers for a chosen MBTI type.
# No external libraries required beyond Streamlit (which Streamlit Cloud provides).

st.set_page_config(page_title="MBTI로 찾는 진로 추천", page_icon="🎯", layout="centered")

st.title("MBTI로 찾는 진로 추천 🎓")
st.markdown("""
안녕하세요! 당신의 MBTI를 골라주면 **해당 유형에 어울리는 2가지 진로**와
각 진로에 적합한 학과(전공) 및 어떤 성격을 가진 사람이 잘 맞는지도 알려줘요.
(이모지는 센스 있게 넣었어요 — 과하진 않게! )
""")

mbti_list = [
    'ISTJ','ISFJ','INFJ','INTJ',
    'ISTP','ISFP','INFP','INTP',
    'ESTP','ESFP','ENFP','ENTP',
    'ESTJ','ESFJ','ENFJ','ENTJ'
]

# Mapping: MBTI -> list of two careers
MBTI_CAREERS = {
    'ISTJ': [
        {
            'career': '공무원 / 행정직',
            'emoji': '🏛️',
            'majors': '행정학, 법학, 경영학',
            'personality': '책임감 있고 규칙을 잘 따르며 세부사항에 강한 사람에게 적합해요.'
        },
        {
            'career': '회계사 / 세무사',
            'emoji': '🧾',
            'majors': '회계학, 경영학, 경영정보',
            'personality': '정확성과 성실성이 뛰어나고 안정적인 환경을 선호하는 사람에게 좋아요.'
        }
    ],
    'ISFJ': [
        {
            'career': '간호사 / 보건의료직',
            'emoji': '🩺',
            'majors': '간호학, 보건학, 응급구조학',
            'personality': '배려심이 많고 사람을 돌보는 걸 좋아하는 사람에게 잘 맞아요.'
        },
        {
            'career': '초등교사 / 교육지원',
            'emoji': '🍎',
            'majors': '유아교육, 초등교육, 교육학',
            'personality': '안정적이고 꾸준히 학생을 돌보는 데 적합해요.'
        }
    ],
    'INFJ': [
        {
            'career': '상담심리사 / 임상심리사',
            'emoji': '🧠',
            'majors': '심리학, 상담심리학',
            'personality': '다른 사람의 감정에 공감하고 깊은 의미를 찾는 사람에게 좋아요.'
        },
        {
            'career': '인문학 연구자 / 작가',
            'emoji': '✍️',
            'majors': '문예창작, 국문학, 철학',
            'personality': '내향적이지만 통찰력 있고 창의적인 작업을 선호하는 분께 추천해요.'
        }
    ],
    'INTJ': [
        {
            'career': '데이터 사이언티스트 / 머신러닝 엔지니어',
            'emoji': '📊',
            'majors': '통계학, 컴퓨터공학, 산업공학',
            'personality': '논리적이고 문제 해결을 즐기며 독립적으로 일하는 걸 좋아하는 사람에게 적합해요.'
        },
        {
            'career': '전략 컨설턴트',
            'emoji': '🧭',
            'majors': '경영학, 경제학, 산업공학',
            'personality': '전체 구조를 설계하고 장기 전략을 세우는 걸 잘하는 분께 좋아요.'
        }
    ],
    'ISTP': [
        {
            'career': '기계공학자 / 현장기술자',
            'emoji': '🔧',
            'majors': '기계공학, 전기공학, 산업공학',
            'personality': '실용적이고 문제를 직접 해결하는 걸 좋아하는 손재주 좋은 사람에게 추천해요.'
        },
        {
            'career': '응급구조대원 / 소방관',
            'emoji': '🚒',
            'majors': '응급구조학, 소방학, 체육학',
            'personality': '즉흥적 판단과 침착함을 발휘해야 할 때 강한 사람에게 잘 맞아요.'
        }
    ],
    'ISFP': [
        {
            'career': '디자이너(시각/패션)',
            'emoji': '🎨',
            'majors': '디자인학과, 패션디자인, 시각디자인',
            'personality': '감각적이고 표현력이 풍부한 사람에게 적절해요.'
        },
        {
            'career': '예술치료사 / 음악치료사',
            'emoji': '🎵',
            'majors': '예술치료, 음악치료, 심리학',
            'personality': '사람을 음악이나 예술로 위로하는 걸 좋아하는 분께 추천해요.'
        }
    ],
    'INFP': [
        {
            'career': '작가 / 편집자',
            'emoji': '📚',
            'majors': '국문학, 문예창작, 커뮤니케이션학',
            'personality': '이상주의적이고 창의적인 내면이 풍부한 사람에게 잘 맞아요.'
        },
        {
            'career': '인권/NGO 활동가',
            'emoji': '🤝',
            'majors': '사회복지학, 국제학, 정치외교학',
            'personality': '가치 지향적이며 사회 문제에 민감한 분께 추천해요.'
        }
    ],
    'INTP': [
        {
            'career': '연구원(이론/컴퓨팅)',
            'emoji': '🔬',
            'majors': '물리학, 수학, 컴퓨터공학',
            'personality': '호기심 많고 논리적 탐구를 즐기는 사람에게 적합해요.'
        },
        {
            'career': 'SW 개발자 / 백엔드 개발자',
            'emoji': '💻',
            'majors': '컴퓨터공학, 소프트웨어학',
            'personality': '문제 분석을 좋아하고 독립적인 작업에 강한 분께 추천해요.'
        }
    ],
    'ESTP': [
        {
            'career': '영업 / 마케팅 실무자',
            'emoji': '💼',
            'majors': '경영학, 광고홍보학, 마케팅',
            'personality': '활동적이고 설득력이 좋아 현장에서 성과를 내는 유형에게 잘 맞아요.'
        },
        {
            'career': '이벤트 기획 / 매니저',
            'emoji': '🎪',
            'majors': '관광학, 서비스경영, 이벤트학',
            'personality': '즉흥적인 상황에 강하고 사람들과 어울리기 좋아하는 분께 추천해요.'
        }
    ],
    'ESFP': [
        {
            'career': '연예/공연 분야(무대스태프 포함)',
            'emoji': '🌟',
            'majors': '연극영화과, 공연예술, 방송영상',
            'personality': '밝고 사교적이며 무대와 사람 앞에서 빛나는 유형에게 좋아요.'
        },
        {
            'career': '호텔/서비스 산업',
            'emoji': '🏨',
            'majors': '관광학, 호텔경영, 서비스경영',
            'personality': '친절하고 고객 응대에 즐거움을 느끼는 분께 추천해요.'
        }
    ],
    'ENFP': [
        {
            'career': '창업가 / 스타트업 실무자',
            'emoji': '🚀',
            'majors': '경영학, 창업학, 디자인씽킹',
            'personality': '아이디어가 많고 사람을 이끄는 데 에너지가 넘치는 분께 잘 맞아요.'
        },
        {
            'career': '콘텐츠 크리에이터 / PR',
            'emoji': '📣',
            'majors': '커뮤니케이션학, 광고홍보학, 미디어학',
            'personality': '창의적이고 사람과 쉽게 공감하는 능력이 있는 분에게 추천해요.'
        }
    ],
    'ENTP': [
        {
            'career': '제품 매니저(PM) / 기획자',
            'emoji': '🧩',
            'majors': '경영학, 산업공학, 컴퓨터공학',
            'personality': '아이디어를 빠르게 실험하고 조율하는 걸 즐기는 분에게 좋아요.'
        },
        {
            'career': '변호사 / 법률가',
            'emoji': '⚖️',
            'majors': '법학, 정치외교학',
            'personality': '토론을 즐기고 논리적 설득에 강한 성향을 가진 분께 추천해요.'
        }
    ],
    'ESTJ': [
        {
            'career': '관리자 / 운영 매니저',
            'emoji': '📋',
            'majors': '경영학, 산업경영, 회계학',
            'personality': '조직을 정리하고 운영하는 걸 잘하는 실무형 리더에게 적합해요.'
        },
        {
            'career': '금융권(심사/영업)',
            'emoji': '🏦',
            'majors': '경영학, 경제학, 금융학',
            'personality': '결정력 있고 규칙을 중요하게 생각하는 분께 추천해요.'
        }
    ],
    'ESFJ': [
        {
            'career': 'HR/인사담당',
            'emoji': '🤝',
            'majors': '경영학, 인사조직, 심리학',
            'personality': '사람을 챙기고 관계 형성에 능한 분에게 잘 맞아요.'
        },
        {
            'career': '의료사회복지사 / 사회복지사',
            'emoji': '🏥',
            'majors': '사회복지학, 간호학, 보건학',
            'personality': '타인을 돕는 데서 보람을 느끼는 분께 추천해요.'
        }
    ],
    'ENFJ': [
        {
            'career': '교사 / 교육 컨설턴트',
            'emoji': '📚',
            'majors': '교육학, 상담심리, 경영학(교육경영)',
            'personality': '사람을 이끌고 성장시키는 걸 좋아하는 외향적 리더에게 적합해요.'
        },
        {
            'career': 'PR / 커뮤니케이션 전문가',
            'emoji': '🗣️',
            'majors': '커뮤니케이션학, 광고홍보학, 미디어학',
            'personality': '공감 능력이 높고 사람을 연결하는 역할에 강해요.'
        }
    ],
    'ENTJ': [
        {
            'career': '경영자 / 기업 임원',
            'emoji': '🏁',
            'majors': '경영학, 경제학, 산업공학',
            'personality': '목표 지향적이고 조직을 이끄는 데 자신있는 사람에게 추천해요.'
        },
        {
            'career': '전략컨설턴트 / 투자분석가',
            'emoji': '📈',
            'majors': '경영학, 경제학, 통계학',
            'personality': '전략적 사고와 빠른 의사결정 능력이 뛰어난 분께 잘 맞아요.'
        }
    ]
}

# User selection
col1, col2 = st.columns([2,1])
with col1:
    mbti = st.selectbox('MBTI를 골라줘 (예: INFP)', mbti_list, index=mbti_list.index('INFP'))
with col2:
    st.write(' ')  # spacing
    st.caption('친구한테 추천해줄 MBTI 골라봐!')

st.divider()

if mbti:
    careers = MBTI_CAREERS.get(mbti.upper())
    if not careers:
        st.warning('아직 그 유형에 대한 데이터가 준비되지 않았어요. 😅')
    else:
        st.subheader(f"{mbti} 유형을 위한 추천 진로 ✨")
        for i, c in enumerate(careers, start=1):
            st.markdown(f"### {i}. {c['emoji']} {c['career']}")
            st.markdown(f"- **어울리는 학과(전공)**: {c['majors']}")
            st.markdown(f"- **어떤 성격이 잘 맞을까?**: {c['personality']}")
            st.write('')

st.divider()

st.info('팁: MBTI는 진로 선택의 *참고용*이에요. 성향을 이해하는 도구로 쓰고, 실제 진로 결정은 다양한 경험과 정보로 해보자! ✨')

st.caption('만들어준 앱을 Streamlit Cloud에 올리면 웹에서 바로 돌려볼 수 있어요. 파일명을 `streamlit_mbti_career.py`로 저장하세요.')
