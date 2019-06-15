from uuid import uuid4

from pymongo import MongoClient

from mantra.db.db_abc import DBTemplete
from mantra.utils.flask_configs import FlaskConfigs
'''
start application
주어지는 정보들
- workspace path
- port
initialize db
get workspace 
get_db
wor
클래스를 만드는데 init에서 ip, port를 받아오고
connect를 해 본 다음에
아무것도 없으면 initial setting을 해 주는 것 까지 한 다음에

기본 기능을 하는 것들이 필요할 것 같다
'''
# conn = pymongo.MongoClient(MONGO_SERVER_IP, MONGO_SERVER_PORT)
# db = conn.AAA
# collection = db.test

# db = conn.get_database('AAA')
# db.create_collection('test')
# collection_list = db.collection_names()
# print(collection_list)

# collection = db.get_collection('test')

class MongoDB(DBTemplete):

    def create_project(self, project_name, project_id, description, category, **kwargs):

        client = MongoClient(FlaskConfigs.db_url())
        db = client.celery_db
        collection = db.projects
        project_info = {
            'project_name': project_name,
            'project_id': project_id,
            'description': description
        }
        collection.insert(project_info)
        results = collection.find({'project_name': project_name})
        client.close()

        return results

