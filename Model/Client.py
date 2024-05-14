from sqlalchemy import Column, Text, DateTime, Integer, ForeignKey
from Model.BaseModel import BaseModel
from sqlalchemy.orm import relationship




class Client(BaseModel):

    __tablename__ = 'clients'

    user_id = Column(Integer, ForeignKey('users.id'))
    client_surname = Column(Text)
    client_name = Column(Text, nullable=False)
    client_patronymic = Column(Text)
    client_date_application = Column(DateTime, nullable=False)
    client_executor = Column(Text)
    nature_of_appeal = Column(Integer)
    result = Column(Text)
    color = Column(Text)

    user = relationship('User', foreign_keys=[user_id])

    def __repr__(self):
        return f"<Client id: {self.id}>"




