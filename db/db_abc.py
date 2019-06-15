import abc

class DBTemplete(abc.ABC):

    @abc.abstractmethod
    def create_project(self, project_name, project_id, description, **kwargs):
        pass

