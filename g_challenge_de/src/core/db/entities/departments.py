from sqlalchemy import Column, Integer, String
from g_challenge_de.src.core.db.db_connect import ENGINE, BASE


class Department(BASE):
    __tablename__ = 'departments'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    department = Column(String, unique=True)

    @staticmethod
    def __delete_schema__():
        '''Delete table'''
        BASE.metadata.tables['departments'].drop(ENGINE)

    @staticmethod
    def __create_schemas__():
        '''Create table'''
        BASE.metadata.create_all(ENGINE)