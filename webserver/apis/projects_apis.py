from flask_restplus import Namespace, Resource, fields
from db.mongo_db import MongoDB
from uuid import uuid4


api = Namespace('projects', description='API for projects')

@api.route('/project')
class Project(Resource):

    def post(self):
        db = MongoDB()
        results = db.create_project('new project', uuid4(), 'comeon~')
        for result in results:
            print(result)
