from sqlalchemy import Column, Text


from Helpers.password import Password
from Model.BaseModel import BaseModel


class User(BaseModel):
    __tablename__ = 'users'

    _guarder = ['password']
    _manual_fillable = ['password']

    login = Column(Text, nullable=False, unique=True)
    password = Column(Text, nullable=False)

    def _manual_fillable_field(self, record: dict):
        if record.get('password') and not record.get('id'):
            self.password = Password().get_hash(record.get('password'))


