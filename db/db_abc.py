import abc

class DBTemplete(abc.ABC):

    @abc.abstractmethod
    def create_user(self, user_name, **kwargs):
        pass

    @abc.abstractmethod
    def create_project(selfs, project_name, project_id, description, **kwargs):
        pass

    @abc.abstractmethod
    def
