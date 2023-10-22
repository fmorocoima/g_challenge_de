from g_challenge_de.src.core.db.entities.jobs import Job
from g_challenge_de.src.core.db.entities.hired_employees import HiredEmployees
from g_challenge_de.src.core.db.entities.departments import Department


ALLOWED_ENTITIES = {
    'jobs': Job,
    'departments': Department,
    'hiredEmployees': HiredEmployees
}


def create_all_schemas():
    Job.__create_all_schemas__()
    HiredEmployees.__create_all_schemas__()
    Department.__create_all_schemas__()
