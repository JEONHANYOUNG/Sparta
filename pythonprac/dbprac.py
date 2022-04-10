from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.h9eiw.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

# 1번 방법
# doc = {
#     'name':'bob',
#     'age':27
# }

# db.users.insert_one(doc)

# 2번 방법
# db.users.insert_one({'name':'bobby','age':27})
# db.users.insert_one({'name':'john','age':20})
# db.users.insert_one({'name':'ann','age':20})

# 일반적으로 많이 사용하는 방식
# doc = {'name':'bob','age':27}
# db.users.insert_one(doc)

# all_users = list(db.users.find({},{'_id':False}))
#
# for user in all_users:
#     print(user)

# user = db.users.find_one({'name':'bobby'})
# print(user['age'])

# Update 방법(name이 'bobby'라는 것을 찾아서 age를 19로 만들어라 라는 의미)
# db.users.update_one({'name':'bobby'},{'$set':{'age':19}})

# Delete 방법(name이 'bobby'라는 것을 찾아서 없애줘라 라는 의미)
# db.users.delete_one({'name':'bobby'})


# - 예시 코드 -
# doc = {'name':'bobby','age':21}
# db.users.insert_one(doc)
#
# # 한 개 찾기 - 예시
# user = db.users.find_one({'name':'bobby'})
#
# # 여러개 찾기 - 예시 ( _id 값은 제외하고 출력)
# all_users = list(db.users.find({},{'_id':False}))
#
# # 바꾸기 - 예시
# db.users.update_one({'name':'bobby'},{'$set':{'age':19}})
#
# # 지우기 - 예시
# db.users.delete_one({'name':'bobby'})