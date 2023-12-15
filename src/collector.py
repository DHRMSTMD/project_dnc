
import requests  # 전체 소스코드
from bs4 import BeautifulSoup  # 원하는 정보 SELECT
from src.service_news import get_news
import pandas as pd
#뉴스 수집(Python) -> Pandas의 데이터프레임 -> Excel 저장
def news_collector(category, page=1, count=1):
    collect_list=[] #향후 데이터프레임 변환용!

    while True:
        #실습용(후에 제거 필수)
        if page == 3:
            break
        url = f"https://news.daum.net/breakingnews/{[category]}?page={page}"
        result = requests.get(url)

        if result.status_code == 200:
            print(result, "접속 성공 → 데이터를 수집합니다.")

            doc = BeautifulSoup(result.text, "html.parser")
            url_list = doc.select("ul.list_news2 a.link_txt")
            # print(f"{page} 페이지의 기사 갯수: {len(url_list)}")

            if len(url_list) == 0:  # 마지막 페이지
                break

            for url in url_list:
                count += 1
                print(f"{count}", "=" * 100)
                # get_news(): 기사 제목, 본문, 날짜 수집 함수
                data = get_news(url["href"], category)
                collect_list.append(data)
        else:
            print("잘못된 URL 경로입니다. 확인 부탁드립니다.")

        page += 1
    #뉴스 수집 완료
    # -collect_list -> dateframe
    col_name = ["category","title", "content", "date"]
    df_review = pd.DataFrame(collect_list, columns=col_name)

    return df_review, count #tuple

