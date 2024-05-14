from classes.BaseClass import BaseClass
from Model.Client import Client as ClientModel


class Client(BaseClass):
    @staticmethod
    def get_model(new_model: bool = False) -> ClientModel:
        return ClientModel() if new_model else ClientModel

