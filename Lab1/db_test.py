from pymongo import MongoClient

#1. Connect to database
client = MongoClient("mongodb://admin1:duy2001x1@ds129066.mlab.com:29066/c4e14_nguyenquangduy")

#2. Get default database
db = client.get_default_database()

#3. Get collection
blog = db['blog']

#4. Insert command
# new_post = {
#     'title' : "Hôm nay trời mưa",
#     'content': "Tối ở nhà code."
# }
# blog.insert_one(new_post) #create

posts = blog.find() #get all post in block
for post in posts:
    print(post)
