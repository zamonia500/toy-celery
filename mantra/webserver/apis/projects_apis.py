from uuid import uuid4

from flask_restplus import Namespace, Resource

from mantra.db.mongo_db import MongoDB as DB

api = Namespace('projects', description='API for projects')

class Parsers():
    project_post_parser = api.parser()
    project_post_parser.add_argument('name', required=True, type=str, location='form')
    project_post_parser.add_argument('description', type=str, location='form')
    project_post_parser.add_argument('category', required=True, type=str, location='form',
                                     choices=['classfication', 'object_detection', 'segmentation'])

@api.route('/project')
class Project(Resource):
    
    @api.expect(Parsers.project_post_parser)
    def post(self):
        args = Parsers.project_post_parser.parse_args()
        db = DB()
        results = db.create_project(args['name'], 
                                    str(uuid4()), 
                                    args['description'], 
                                    args['category'])
        for result in results:
            print(result)