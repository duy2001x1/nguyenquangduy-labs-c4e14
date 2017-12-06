from pymongo import MongoClient

client = MongoClient("mongodb://admin:admin@ds021182.mlab.com:21182/c4e")

db = client.get_default_database()

pun = db['posts']

new_post = {
    'title': "Just a Random Rap Punchline",
    'artist': "Quang Duy",
    'content': '''Danh tiếng chúng mày cũng chỉ là cái mác/Mac
    Cho nên trận này chúng mày đ*o có win đâu/Windows'''
}

pun.insert_one(new_post)

posts = pun.find()
for post in posts:
    print(post)
