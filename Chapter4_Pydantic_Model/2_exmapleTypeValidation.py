from pydantic import BaseModel
from typing import Optional, TypedDict, List, Dict

class Patient(BaseModel):
    name:str
    age: int
    weight: float
    married: bool
    allergies: Optional[List[str]] = None
    contacts: Dict[str, str]

def insert_patient_info(patient:Patient):
    print(patient.name)
    print(patient.age)
    print("Insertion successfully")

def update_patient_info(patient:Patient):
    print(patient.name)
    print(patient.age)
    print("Updation successfully")


class PatientData(TypedDict):
    name: str
    age: int
    weight: float
    married: bool
    allergies: Optional[List[str]]
    contacts: Dict[str, str]

patient_data: PatientData = {"name": "Tom", "age": 45, "weight": 70.5, "married": False, "contacts": {"email": "tom@example.com"}}
patient_data2: PatientData = {"name": "Bhim", "age": 45, "weight": 80.0, "married": True, "allergies": ["shellfish"], "contacts": {"email": "bhim@example.com"}}

patient1 = Patient(**patient_data)
patient2 = Patient(**patient_data2)

insert_patient_info(patient1)
update_patient_info(patient2)