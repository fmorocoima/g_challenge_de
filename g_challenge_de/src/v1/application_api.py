from fastapi import File, UploadFile
from g_challenge_de.src.core.schemas import (InsertJob, InsertDepartment, InsertHiredEmployees)
from fastapi import APIRouter
from g_challenge_de.src.core.db.entities.jobs import Job
from g_challenge_de.src.core.db.entities.departments import Department
from g_challenge_de.src.core.db.entities.hired_employees import HiredEmployees
from g_challenge_de.src.core.db.create_schemas import ALLOWED_ENTITIES

router = APIRouter()

@router.post("/import-from-csv/{entity}/", tags=["Import"])
async def upload_job_csv(entity: str, file: UploadFile = File(...)):
    '''
    <h3>Allowed values for entity:</h3>
    <ul>
        <li>jobs</li>
        <li>departments</li>
        <li>hiredEmployees</li>
    </ul>
    '''
    if entity not in ALLOWED_ENTITIES.keys():
        return {"response": f"Entity '{entity}' found"}
    entity_obj = ALLOWED_ENTITIES[entity]
    response = await entity_obj.insert_from_csv(file)
    return {"response": response}


@router.post("/insert/job/", tags=["Job"])
async def insert_job(body_params : InsertJob):
    '''
    <h3>Input structure:</h3>

        [
            {
            "id": int,
            "job": string
            },
        ]

    <h3>Output structure:</h3>

        {
        "valids": [
            {
            "id": int,
            "job": string
            }
        ],
        "invalids": []
        }
    '''
    result = await Job.insert_jobs(body_params.jobs)
    return result


@router.post("/insert/department/", tags=["Department"])
async def insert_department(body_params : InsertDepartment):
    '''
    <h3>Input structure:</h3>

        {
            "departments" : [ {"id": int, "department": string},... ]
        }

    <h3>Output structure:</h3>

        {
        "valids": [
            {
            "id": int,
            "job": string
            }
        ],
        "invalids": []
        }
    '''
    result = await Department.insert_departments(body_params.departments)
    return result

@router.post("/insert/hired-employees/", tags=["Hired employees"])
async def insert_hired_employee(body_params : InsertHiredEmployees):
    '''
    <h3>Input structure:</h3>

        {
        "hired_employees": [
            {
            "id": int,
            "name": string,
            "department_id": int,
            "job_id": int
            }
        ]
        }

    <h3>Output structure:</h3>

        {
        "valids": [
            {
            "id": int,
            "job": string
            }
        ],
        "invalids": []
        }
    '''
    result = await HiredEmployees.insert_hired_employees(body_params.hired_employees)
    return result
