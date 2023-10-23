from fastapi import File, UploadFile
from g_challenge_de.src.core.schemas import (InsertJob, InsertDepartment, InsertHiredEmployees)
from fastapi import APIRouter
from g_challenge_de.src.core.db.entities.jobs import Job
from g_challenge_de.src.core.db.entities.departments import Department
from g_challenge_de.src.core.db.entities.hired_employees import HiredEmployees
from g_challenge_de.src.core.db.create_schemas import ALLOWED_ENTITIES

router = APIRouter()

@router.post("/import-from-csv/{entity}/", tags=["Section 1: API"])
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


@router.post("/insert/job/", tags=["Section 1: API"])
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


@router.post("/insert/department/", tags=["Section 1: API"])
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

@router.post("/insert/hired-employees/", tags=["Section 1: API"])
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


@router.get("/hired-employees-by-quarter/", tags=["Section 2: SQL"])
async def get_hired_employees_by_quarter(year: int = 2021):
    '''
    <h3>Requirements Description:</h3>
    <h4>Number of employees hired for each job and department in the sellected year (default 2021)  divided by quarter. 
    The response is alphabetically ordered by department and job.
    </h4>
    <h3>Input value:</h3>
        
        year: int
    
    <h3>Output example:</h3>

        {
            "valids": [
                {
                    "department": "Accounting",
                    "job": "Account Representative IV",
                    "Q1": 1,
                    "Q2": 0,
                    "Q3": 0,
                    "Q4": 0
                    },
                ],
            "invalids": []
        }
    '''
    result = await HiredEmployees.get_by_quarter(year)
    return result

@router.get("/hired-employees-above-average/", tags=["Section 2: SQL"])
async def get_hired_employees_above_average(year: int = 2021):
    '''
    <h3>Requirements Description:</h3>
    <h4>List of ids, name and number of employees hired of each department that hired more
    employees than the mean of employees hired in the sellected year (default 2021) for all the departments, ordered
    by the number of employees hired (descending)..
    </h4>
    <h3>Input value:</h3>
        
        year: int

    <h3>Output example:</h3>
    
        {
            "valids": [
                    {
                      "id": 3,
                      "department": "Research and Development",
                      "hired": 177
                    },
                ],
            "invalids": []
        }
    '''
    result = await HiredEmployees.get_departments_above_average(year)
    return result