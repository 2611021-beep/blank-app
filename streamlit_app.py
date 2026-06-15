import streamlit as st

# 1. 데이터 정의 (기존 코드의 로직 그대로 유지)
chemical = ['염산', '암모니아', '에탄올']
danger = ['피부와 접촉시 따가움 유발', '유독 가스 생성', '불이 매우 잘붙음']
storage = ['폐쇄된곳에 보관', '환기가 잘되는곳에 보관', '화기가 없는곳에 보관']

# 2. 웹 앱 타이틀 및 UI 구성
st.title("🧪 화학물질 안전 프로그램")
st.write("조회하고 싶은 화학물질을 선택하거나 입력하여 위험성 및 보관방법을 확인하세요.")

st.divider()  # 시각적인 구분선

# 3. 입력 위젯 (기존 input을 스트림릿 위젯으로 변경)
# 사용자가 오타 없이 쉽게 선택할 수 있도록 selectbox를 제공하되, 직접 입력도 가능하게 '직접 입력' 옵션을 추가했습니다.
search_option = st.selectbox(
    "화학물질을 선택하세요:", 
    options=["선택하세요"] + chemical + ["직접 입력"]
)

# '직접 입력'을 선택했을 때만 텍스트 입력창이 나타나도록 처리
if search_option == "직접 입력":
    search_query = st.text_input("화학물질 이름을 정확히 입력하세요:")
else:
    search_query = search_option

# 검색 버튼
search_button = st.button("🔍 정보 조회하기")

# 4. 출력 및 핵심 로직 섹션 (기존 print문과 조건문을 스트림릿 결과 창으로 변경)
if search_button:
    if search_query == "선택하세요" or search_query == "":
        st.warning("⚠️ 화학물질을 선택하거나 입력해주세요.")
    else:
        found = False
        
        # 화학물질 데이터 검색
        for i in range(len(chemical)):
            if search_query == chemical[i]:
                # 정보를 찾았을 때 깔끔한 가독성을 위해 st.success와 카드 형태(metric) 등으로 출력
                st.success(f"### 💡 {chemical[i]} 안전 정보")
                
                col1, col2 = st.columns(2)
                with col1:
                    st.error(f"🚨 **위험성**\n\n{danger[i]}")
                with col2:
                    st.info(f"📦 **보관방법**\n\n{storage[i]}")
                
                found = True
                break
        
        # 정보를 찾지 못했을 때
        if not found:
            st.error(f"❌ '{search_query}'에 대한 화학물질 정보가 시스템에 없습니다.")