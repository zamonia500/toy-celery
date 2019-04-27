from flask_restplus import Api

from .upload_image_apis import api as upload_image_api

api = Api(
    title='Toy-Celery-Backend',
    version='1.0',
    description='This is just toy project for my pleasure'
)

# aggregate APIs
api.add_namespace(upload_image_api)
