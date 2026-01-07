from pydantic import BaseModel, EmailStr,field_validator, model_validator
from typing import Optional, TypedDict, List, Dict

class Patient(BaseModel):
    name:str
    age: int
    weight: float 
    email : EmailStr
    married: bool 
    allergies: Optional[List[str]] = None
    contacts: Dict[str, str]

    @model_validator(mode='after')  #@model_validator: A decorator that allows defining validation logic that applies to the entire model before or after field-level validation.
    def valdate_emergency_contact(cls, model):
        if model.age > 60 and 'emergency' not in model.contacts:
            raise ValueError('Emergency contact is required in contacts for patients over 60 years old')
        return model 

    @field_validator('email')   #@field_validator: A decorator used to define custom validation logic for specific fields.It intercepts field values before they are assigned and can transform or validate them.
    @classmethod                #@classmethod: A decorator that binds a method to the class rather than an instance,allowing access to class-level data and enabling reusable validation across all instances.
    def validate_email(cls, v):
        valid_domains = ['hdfc.com','icici.com']
        domain_name = v.split('@')[-1]
        if domain_name not in valid_domains:
            raise ValueError(f'Email domain must be one of the following: {", ".join(valid_domains)}')
        return v
    
    @field_validator('name')
    @classmethod
    def validate_name(cls, v):
        return v.upper()

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
    email : EmailStr
    married: bool
    allergies: Optional[List[str]]
    contacts: Dict[str, str]

patient_data: PatientData = {"name": "Tom", "age": 65, "weight": 70.5, "email": "tom@icici.com", "married": False, "contacts": {"email": "tom@example.com", "emergency": "1234567890"}}
patient_data2: PatientData = {"name": "Bhim", "age": 45, "weight": 80.0, "email": "bhim@hdfc.com", "married": True, "allergies": ["shellfish"], "contacts": {"email": "bhim@example.com"}}

patient1 = Patient(**patient_data)
patient2 = Patient(**patient_data2)

insert_patient_info(patient1)
update_patient_info(patient2)