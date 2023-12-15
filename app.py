#Streamlit 라이브러리
# Python으로 손쉽게 웹사이트를 생성할 수 있는 라이브러리
# HTML,CSS, JS 등과 같은 기술을 공부해야 웹사이트 구현가능
#- Streamlit을 사용하면 위의 기술을 모르더라도 블럭 쌓듯이 손쉽게 구현 가능
# 단점은 우리가 원하는 디테일한 작업 불가능
# 터미널->streamlit run ./app.py
# .. 위로 . 현재 ./ 아래
import streamlit as st
from src.collector import news_collector
from datetime import datetime
import pyarrow as _lib
import pyarrow as pa
news_category ={

    "society":   "사회",
    "politics":   "정치",
    "economic":   "경제",
    "foreign":   "국제",
    "culture":   "문화",
    "entertain":   "연예",
    "sports": "스포츠",
    "digital":     "IT"

}
# st.set_page-config(
#     page_title="뉴스 수집기",
#     page_icon"./images.favicon_01.png"
# )

st.title(":red[NEWS] COLLECTOR")
st.text("DAUM 뉴스를 수집합니다.")
def convert_df(df):
    return df.to_csv(index=False, encoding="cp949")
flag = False
with st.form(key="form"):
    category = st.text_input("카테고리 입력하세요.").strip()
    submitted = st.form_submit_button("Submit")

    if submitted: #"Submit" 버튼을 누르면!
        if category in list(news_category.keys()):
            #뉴스 수집!
           st.write(f'"{news_category[category]}"뉴스를 수집합니다.')
           df_review,count = news_collector(category)
           #dataframe -> csv 형식
           csv=convert_df(df_news)
           flag = True


        else:
            st.write("올바른 뉴스 카테고리 입력.")
if flag:
    st.write(f'"{news_category[category]}"뉴스 {count}건 수집 완료.')
    now = datetime.now().strftime("%Y_%m_%d_%H%M%S")
    st.download_button(
        label="Press to Download",

        data=csv,
        mime = "text/csv",
        file_name=f"{news_category[category]}_뉴스_{now}" #스포츠 _뉴스_20231215.csv
    )

