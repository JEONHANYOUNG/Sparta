from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.h9eiw.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

# 1. 가버나움 영화의 평점 구하기
# movie = db.movies.find_one({'title':'가버나움','rank':'03'})
# print(movie['star'])

# 2. 가버나움의 평점과 같은 평점의 영화제목들 가져오기
# movie = db.movies.find_one({'star':'9.59'})
# star = movie['star']
#
# all_movies = list(db.movies.find({'star':star},{'_id':False}))
#
# for movie in all_movies:
#     print(movie['title'])

# 3. 가버나움 영화의 평점을 0으로 만들기(원래 평점은 9.59)
# db.movies.update_one({'title':'가버나움'},{'$set':{'star':'0'}})