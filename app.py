import streamlit as st
import pandas as pd

# 페이지 기본 설정
st.set_page_config(page_title="무대 연출 맞춤형 가이드", page_icon="🎤")

st.title("🎤 무대 연출 맞춤형 가이드 앱")
st.write("공연 컨셉, 장르, 인원수를 선택하면 최적의 의상·대형·조명을 추천해 드립니다.")
st.divider()

# 1. 리스트(List): 추천 항목 및 선택지 정리
recommend_categories = ["의상(옷)", "대형", "조명", "장르별 연출 포인트"]
concepts = ["청량", "카리스마", "몽환", "레트로", "힙합"]
genres = ["댄스", "발라드", "밴드"]

st.info(f"**추천 가능 항목:** {', '.join(recommend_categories)}")

# 2. 함수(Function): 웹 UI에서 무대 컨셉과 장르를 선택받는 함수
def select_stage_theme():
    col1, col2 = st.columns(2)
    with col1:
        concept = st.selectbox("원하는 무대 컨셉을 선택하세요", concepts)
    with col2:
        genre = st.selectbox("공연 장르를 선택하세요", genres)
    return concept, genre

# 함수 호출 및 인원 입력 (최소 1명 이상)
selected_concept, selected_genre = select_stage_theme()
member_count = st.number_input("무대에 오르는 인원수를 입력하세요", min_value=1, max_value=50, value=5, step=1)

# 버튼 클릭 시 결과 생성
if st.button("✨ 맞춤형 무대 가이드 생성하기", type="primary"):
    # 3. 조건문(if-elif-else): 인원수, 컨셉, 장르별 맞춤형 추천
    if member_count == 1:
        formation = "솔로 무대 (중앙 집중형 동선)"
    elif member_count <= 5:
        formation = "소인원 대형 (다이아몬드형 및 1열 교차 대형)"
    else:
        formation = "다인원 대형 (V자 대형, 2단 피라미드 및 칼군무 웨이브 대형)"

    if selected_concept == "청량":
        outfit = "하얀색 셔츠와 연청 데님 팬츠"
        lighting = "하얀색과 파란색(스카이블루) 조명을 섞어서 시원한 느낌 연출"
    elif selected_concept == "카리스마":
        outfit = "블랙 레더 재킷과 워커 부츠"
        lighting = "강렬한 빨간색 핀조명과 빠른 스트로보 효과"
    elif selected_concept == "몽환":
        outfit = "파스텔톤 쉬폰 셔츠와 실버 액세서리"
        lighting = "보라색과 분홍색 그라데이션 조명 및 안개(스모그) 효과"
    elif selected_concept == "레트로":
        outfit = "체크 패턴 재킷, 나팔바지 및 컬러 선글라스"
        lighting = "따뜻한 노란색(웜톤)과 오렌지색을 섞은 미러볼 스타일 조명"
    else:  # 힙합
        outfit = "오버핏 후드티, 카고 팬츠 및 비니/볼캡"
        lighting = "네온 그린과 짙은 파란색 조명을 교차해 역동적인 분위기 연출"

    if selected_genre == "댄스":
        genre_tip = "동선 이동이 많으므로 무대 바닥을 넓게 쓰고 비트에 맞춰 조명을 점멸시킬 것"
    elif selected_genre == "발라드":
        genre_tip = "보컬 감정 전달을 위해 스탠드 마이크를 활용하고 후렴구에서 핀조명을 집중시킬 것"
    else:  # 밴드
        genre_tip = "악기 배치(드럼 중앙, 기타/베이스 좌우)를 고정하고 연주자별 개별 조명을 세팅할 것"

    # 4. 반복문(for문)을 활용해 표(Table) 데이터 가공
    raw_summary = [
        ["무대 컨셉", selected_concept],
        ["공연 장르", selected_genre],
        ["참여 인원", f"{member_count}명"],
        ["추천 의상", outfit],
        ["추천 대형", formation],
        ["추천 조명", lighting],
        ["장르 연출 팁", genre_tip]
    ]

    table_rows = []
    for row in raw_summary:
        table_rows.append({"항목": row[0], "추천 가이드 내용": row[1]})

    # 표 형태로 출력
    st.subheader("📋 무대 연출 총정리 표")
    df = pd.DataFrame(table_rows)
    st.table(df)

    # 5. 최종 요약 멘트 출력
    st.subheader("💡 최종 추천 멘트")
    st.success(
        f"**'{selected_concept}'** 컨셉의 **{selected_genre}** 무대(**{member_count}명**)를 준비하시는군요!\n\n"
        f"인원에 맞춰 **{formation}**을(를) 활용하시고, 의상은 **{outfit}** 스타일을 추천합니다. "
        f"조명은 **{lighting}**하는 것이 좋을 것 같고, {selected_genre} 무대 특성상 **{genre_tip}**!"
    )
