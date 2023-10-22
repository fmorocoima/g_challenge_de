from typing import Optional, Union, List
from pydantic import BaseModel

#----------------------------------Jobs---------------------------------

class JobStructure(BaseModel):
    id: Optional[Union[int, None]]
    job: str

class InsertJob(BaseModel):
    """
    Params to insert a new Job to the list.
    """
    jobs : List[JobStructure]

#----------------------------------Department---------------------------------

class DepartmentStructure(BaseModel):
    id: Optional[Union[int, None]]
    department: str

class InsertDepartment(BaseModel):
    """
    Params to insert a new Department to the list.
    """
    departments : List[DepartmentStructure]


#----------------------------------HiredEmployees---------------------------------

class HiredEmployeesStructure(BaseModel):
    id: Optional[Union[int, None]]
    name: str
    department_id: Optional[Union[int, None]]
    job_id: Optional[Union[int, None]]

class InsertHiredEmployees(BaseModel):
    """
    Params to insert a new Department to the list.
    """
    hired_employees : List[HiredEmployeesStructure]