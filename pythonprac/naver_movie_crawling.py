import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.h9eiw.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

# headers => 브라우저에서 콜을 날린 것처럼 해주는 것, url은 필요할 때마다 바꿔서 사용 가능
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=pnt&date=20210829',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

# 하나만 select 한 것
# title = soup.select_one('#old_content > table > tbody > tr:nth-child(2) > td.title > div > a')
# print(title['href'])

#old_content > table > tbody > tr:nth-child(3) > td.title > div > a
#old_content > table > tbody > tr:nth-child(4) > td.title > div > a

movies = soup.select('#old_content > table > tbody > tr')

# 리스트의 구조
# for movie in movies:
#     a = movie.select_one('td.title > div > a')
#     if a is not None:
#         None => 가로선
#         print(a.text)

for movies in movies:
    a= movies.select_one('td.title > div > a')
    if a is not None:
        title = a.text
        rank = movies.select_one('td:nth-child(1) > img')['alt']
        star = movies.select_one('td.point').text
        # print(title,rank,star)
        doc = {
            'title':title,
            'rank':rank,
            'star':star
        }
        db.movies.insert_one(doc)