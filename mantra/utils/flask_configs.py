from flask import current_app

class FlaskConfigs(object):

    @classmethod
    def db_url(cls):
        return current_app.config['DATABASE_URL']