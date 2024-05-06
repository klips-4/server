
from sqlalchemy import Column, Text, DateTime, Integer
from Model.BaseModel import BaseModel


class Client(BaseModel):
    __tablename__ = 'clients'

    id = Column(Integer, primary_key=True)
    client_surname = Column(Text)
    client_name = Column(Text, nullable=False)
    client_patronymic = Column(Text)
    client_date_application = Column(DateTime, nullable=False)
    client_executor = Column(Text)
    nature_of_appeal = Column(Integer)
    result = Column(Text)

    def __init__(self, *args, **kwargs):
        super(Client, self).__init__(*args, **kwargs)

    def __repr__(self):
        return f"<Client id: {self.id}"
