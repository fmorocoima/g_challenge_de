from sqlalchemy import Column, Integer, String
from g_challenge_de.src.core.db.db_connect import ENGINE, BASE



class Job(BASE):
    __tablename__ = 'jobs'

    id = Column(Integer, primary_key=True, autoincrement=True)
    job = Column(String, unique=True)

    @staticmethod
    def __delete_schema__():
        '''Delete table'''
        BASE.metadata.tables['jobs'].drop(ENGINE)

    @staticmethod
    def __create_schema__():
        '''Create table'''
        BASE.metadata.create_all(ENGINE)
