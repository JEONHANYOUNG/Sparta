# 1. print('hello sparta!!')
#    => hello sparta!!

# 2. a=2
#    b=3
#    print(a+b)
#  => 5

# 3. a='hy'
#    b='c'
#    print(a+b)
#  => hyc

# 4. a_list = ['사과','배','감']
#    print(a_list[1])
#  => 배

# a_list에 추가하는 것은 .append()

# a_list = ['사과','배','감']

# a_list.append('수박')

# print(a_list)
# ['사과', '배', '감', '수박']

# a_dict = {
#     'name':'bob',
#     'age':27
# }

# print(a_dict['name'])
# => bob

# 함수
# def sum(a,b):
#     print('더하자!')
#     return a+b 이거로 결과를 변화하는 것
#     => 더하자!

# result = sum(1,2)
# print(result)
# => 3

# 조건문
# def is_adult(age): <- 이거 다음 항목은 if문에 담긴 내용물이다.
#     if age > 20;
#         print('성인입니다')
#     else:
#         print('청소년입니다')

# is_adult(15)
# => 청소년입니다

# 반복문
# fruits = ['사과','배','배','감','수박','귤','딸기','사과','배','수박']

# count = 0               <= count 가 0부터 시작한다.
# for fruit in fruits:     <= 리스트의 요소들을 하나씩 꺼내서 내용물로 해서 쓴다
# 	if fruit == '사과':   <= fruit 가 만약 사과라면
		# count += 1        <= count를 하나 늘려줘라는 읨읨
# print(count)
# => 2

# 사과의 갯수를 세어 보여줍니다.

# 리스트 형식
# people = [{'name': 'bob', 'age': 20},
#           {'name': 'carry', 'age': 38},
#           {'name': 'john', 'age': 7},
#           {'name': 'smith', 'age': 17},
#           {'name': 'ben', 'age': 27}]
# => bob

# 모든 사람의 이름과 나이를 출력해봅시다.
# for person in people:
#     print(person['name'], person['age'])

# bob 20
# carry 38
# john 7
# smith 17
# ben 27

# 이번엔, 반복문과 조건문을 응용한 함수를 만들어봅시다.
# 이름을 받으면, age를 리턴해주는 함수
# def get_age(myname):
#     for person in people:
#         if person['name'] == myname:
#             return person['age']
#     return '해당하는 이름이 없습니다'


# print(get_age('bob'))    <= 20
# print(get_age('kay'))    <= 해당하는 이름이 없습니다

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