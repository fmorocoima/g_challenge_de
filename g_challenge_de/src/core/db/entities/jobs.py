from sqlalchemy import Column, Integer, String, insert
from g_challenge_de.src.core.db.db_connect import ENGINE, BASE, execute
import csv


class Job(BASE):
    __tablename__ = 'jobs'

    id = Column(Integer, primary_key=True, autoincrement=True)
    job = Column(String, unique=True)

    @staticmethod
    def __delete_schema__():
        '''Delete table'''
        BASE.metadata.tables['jobs'].drop(ENGINE)

    @staticmethod
    def __create_all_schemas__():
        '''Create table'''
        BASE.metadata.create_all(ENGINE)

    @staticmethod
    async def insert_from_csv(file):
        result = {'valids': [], 'invalids': []}
        f_content = await file.read()

        if file.filename.lower().endswith('.csv'):
            to_insert = []
            csv_content = f_content.decode('utf-8').replace('\r\n', '\n').split('\n')

            for line in csv_content:
                elements = line.split(',')
                if len(elements) == 2:
                    try:
                        job_id = int(elements[0])
                        job_name = elements[1]

                        # Insert the job record into the database
                        stmt = insert(Job).values(id=job_id, job=job_name).returning(Job)
                        query_result = execute(stmt).fetchall()

                        if query_result:
                            job_record = query_result[0]
                            to_insert.append({'id': job_record.id, 'job': job_record.job})
                        else:
                            result['invalids'].append({'id': job_id, 'job': job_name})
                    except Exception as e:
                        result['invalids'].append({'id': job_id, 'job': job_name})
                    print(elements)

            result['valids'] = to_insert

        return result
    

    @staticmethod
    async def insert_jobs(jobs: list):
        result = {'valids':[], 'invalids':[]}
        to_insert = []
        obj = {}
        for element in jobs:
            if element.id:
                obj['id'] = element.id
            obj['job'] = element.job
            try:
                stmt = insert(Job).values(**obj).returning(Job)
                query_result = execute(stmt).fetchone()
                to_insert.append({
                    'id':int(query_result[0]),
                    'job':str(query_result[1])
                    }
                )
            except Exception as e:
                result['invalids'].append(
                    {'id':element.id, 'job':element.job}
                )
            print(element)
        result['valids'] = to_insert
        return result
