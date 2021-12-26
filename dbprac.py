from pymongo import MongoClient
client = MongoClient('mongodb+srv://sparta:<pw>@cluster0.8s2if.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbhandey

# doc = {
#     'name':'ssona',
#     'age':25
# }

#
# db.users.insert_one({'name':'scott','age':30})
# db.users.insert_one({'name':'pam','age':26})
# db.users.insert_one({'name':'emma','age':24})


user = db.users.find_one({'name':'pam'});
# print(user['age']);


# all_users = list(db.users.find({}, {'_id':False}));
# for user in all_users:
#     print(user);


# db.users.update_one({'name':'ssona'},{'$set':{'age':63}})


# db.users.delete_one({'name':'emma'});




# 저장 - 예시
doc = {'name':'bobby','age':21}
db.users.insert_one(doc)

# 한 개 찾기 - 예시
user = db.users.find_one({'name':'bobby'})

# 여러개 찾기 - 예시 ( _id 값은 제외하고 출력)
all_users = list(db.users.find({},{'_id':False}))

# 바꾸기 - 예시
db.users.update_one({'name':'bobby'},{'$set':{'age':19}})

# 지우기 - 예시
db.users.delete_one({'name':'bobby'})