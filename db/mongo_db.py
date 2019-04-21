'''
start application
주어지는 정보들
- workspace path
- port
initialize db
get workspace 
get_db
wor
'''
import pymongo
MONGO_SERVER_IP = '127.0.0.1'
MONGO_SERVER_PORT = 27017 # mongoDB default port

conn = pymongo.MongoClient(MONGO_SERVER_IP, MONGO_SERVER_PORT)
db = conn.AAA
collection = db.test

db = conn.get_database('AAA')
db.create_collection('test')
collection_list = db.collection_names()
print(collection_list)

collection = db.get_collection('test')
