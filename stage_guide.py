# 1. 리스트(List): 추천 항목 및 선택지 (컨셉 2개 추가!)
recommend_categories = ["의상(옷)", "대형", "조명", "장르별 연출 포인트"]
concepts = ["청량", "카리스마", "몽환", "레트로", "힙합"]
genres = ["댄스", "발라드", "밴드"]

# 2. 함수(Function): 무대 컨셉과 장르를 선택받는 함수
def select_stage_theme():
    print("=== [무대 연출 맞춤형 가이드] ===")
    print("추천 가능 항목:", ", ".join(recommend_categories))
    print("-" * 45)
    
    while True:
        print(f"선택 가능한 컨셉: {concepts}")
        concept = input("원하는 무대 컨셉을 입력하세요: ").strip()
        if concept in concepts:
            break
        print("목록에 있는 컨셉 중에서 정확히 입력해주세요!\n")
        
    while True:
        print(f"선택 가능한 장르: {genres}")
        genre = input("공연 장르를 입력하세요: ").strip()
        if genre in genres:
            break
        print("목록에 있는 장르 중에서 정확히 입력해주세요!\n")
        
    return concept, genre

# 실행 부분: 함수 호출 및 인원 입력
selected_concept, selected_genre = select_stage_theme()
member_count = int(input("무대에 오르는 인원수를 숫자로 입력하세요: "))

# 3. 조건문(if-elif-else): 인원수, 컨셉, 장르별 맞춤형 추천
# (1) 인원수에 따른 대형 추천
if member_count == 1:
    formation = "솔로 무대 (중앙 집중형 동선)"
elif member_count <= 5:
    formation = "소인원 대형 (다이아몬드형 및 1열 교차 대형)"
else:
    formation = "다인원 대형 (V자 대형, 2단 피라미드 및 칼군무 웨이브 대형)"

# (2) 컨셉에 따른 의상 및 조명 추천 (5가지 컨셉)
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

# (3) 장르에 따른 무대 연출 포인트 추천
if selected_genre == "댄스":
    genre_tip = "동선 이동이 많으므로 무대 바닥을 넓게 쓰고 비트에 맞춰 조명을 점멸시킬 것"
elif selected_genre == "발라드":
    genre_tip = "보컬 감정 전달을 위해 스탠드 마이크를 활용하고 후렴구에서 핀조명을 집중시킬 것"
else:  # 밴드
    genre_tip = "악기 배치(드럼 중앙, 기타/베이스 좌우)를 고정하고 연주자별 개별 조명을 세팅할 것"

# 4. 반복문(for문)을 활용해 표(Table) 형태로 출력할 리스트 구성
summary_table = [
    ["무대 컨셉", selected_concept],
    ["공연 장르", selected_genre],
    ["참여 인원", f"{member_count}명"],
    ["추천 의상", outfit],
    ["추천 대형", formation],
    ["추천 조명", lighting],
    ["장르 연출 팁", genre_tip]
]

print("\n" + "=" * 75)
print(f"{'항목':<12} | {'추천 가이드 내용'}")
print("=" * 75)

# for문으로 리스트를 순회하며 표 형식으로 출력
for row in summary_table:
    category = row[0]
    detail = row[1]
    print(f"{category:<12} | {detail}")

print("=" * 75)

# 5. 최종 요약 문장 출력
print("\n[최종 추천 멘트]")
print(f"'{selected_concept}' 컨셉의 {selected_genre} 무대({member_count}명)를 준비하시는군요!")
print(f"인원에 맞춰 '{formation}'을(를) 활용하시고, 의상은 {outfit} 스타일을 추천합니다.")
print(f"조명은 {lighting}하는 것이 좋을 것 같고, {selected_genre} 무대 특성상 {genre_tip}!")
