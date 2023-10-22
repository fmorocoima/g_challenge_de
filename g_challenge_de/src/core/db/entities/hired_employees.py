from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, insert
from g_challenge_de.src.core.db.db_connect import ENGINE, BASE, SESSION, execute
from datetime import datetime
import csv


class HiredEmployees(BASE):
    __tablename__ = 'hired_employees'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True)
    datetime = Column(DateTime, default=datetime.utcnow)
    department_id = Column(Integer, ForeignKey('departments.id'))
    job_id = Column(Integer, ForeignKey('jobs.id'))

    @staticmethod
    def __delete_schema__():
        '''Delete table'''
        BASE.metadata.tables['hired_employees'].drop(ENGINE)

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
            csv_lines = f_content.decode(
                'utf-8').replace('\r\n', '\n').split('\n')

            for line in csv_lines:
                if not line:
                    continue
                elements = line.split(',')

                try:
                    id = int(elements[0])
                    name = elements[1]
                    datetime = elements[2] if elements[2] else None
                    department_id = int(
                        elements[3]) if elements[3].isdigit() else None
                    job_id = int(
                        elements[4]) if elements[4].isdigit() else None

                    stmt = insert(HiredEmployees).values(
                        id=id,
                        name=name,
                        datetime=datetime,
                        department_id=department_id,
                        job_id=job_id
                    ).returning(HiredEmployees)

                    query_result = execute(stmt).fetchone()

                    to_insert.append({
                        'id': query_result[0],
                        'name': query_result[1],
                        'datetime': query_result[2],
                        'department_id': query_result[3] if isinstance(query_result[3], int) else None,
                        'job_id': query_result[4] if isinstance(query_result[4], int) else None
                    })
                except Exception as e:
                    result['invalids'].append({
                        'id': elements[0],
                        'name': elements[1],
                        'datetime': elements[2],
                        'department_id': elements[3],
                        'job_id': elements[4]
                    })
                print(line)

        result['valids'] = to_insert
        return result
    
    @staticmethod
    async def insert_hired_employees(hired_employees: list):
        result = {'valids':[], 'invalids':[]}
        to_insert = []
        obj = {}
        for element in hired_employees:
            if element.id:
                obj['id'] = element.id
            if element.department_id:
                obj['department_id'] = element.department_id
            if element.job_id:
                obj['job_id'] = element.job_id
            obj['name'] = element.name
            try:
                stmt = insert(HiredEmployees).values(**obj).returning(HiredEmployees)
                query_result = execute(stmt).fetchone()
                to_insert.append({
                    'id': int(query_result[0]),
                    'name': str(query_result[1]),
                    'datetime': str(query_result[2]),
                    'department_id': int(query_result[3]) if isinstance(query_result[3], int) else None,
                    'job_id': int(query_result[4]) if isinstance(query_result[4], int) else None
                    }
                )
            except Exception as e:
                    result['invalids'].append(obj)
            print(element)
        result['valids'] = to_insert
        return result

