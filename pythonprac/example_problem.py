# 예제 문제
# import requests # requests 라이브러리 설치 필요

# r = requests.get('http://spartacodingclub.shop/sparta_api/seoulair')
# rjson = r.json()

# rows = rjson['RealtomeCityAir']['row']

# for row in rows:
    # gu_name = row['MSRSTE_NM']   <= gu_name은 row의 'MSRSTE_NM'
    # gu_mise = row['IDEX_MVL']    <= gu_mise는 row의 'IDEX_MVL'

    # 1. 지역 구와 미세먼지 두개 항목에 대해 값 출력
    # print(gu_name,gu_mise)

    # 2. 미세먼지가 40보다 작으면 값 출력
    # if gu_mise < 40:
        # print(gu_name)

# print(rjson)