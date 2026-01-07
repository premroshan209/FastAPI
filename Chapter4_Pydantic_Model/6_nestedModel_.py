# nested Pydantic model : nested pydantic models allow you to create complex data structures by embedding one model within another. 
# This is useful for representing hierarchical or related data in a clear and organized manner.

from pydantic import BaseModel

class Address(BaseModel):
    city: str
    state: str
    pin: str

class Patient(BaseModel):
    name: str
    age: int
    gender: str
    address: Address  # Nested Pydantic model


address_dict = {"city": "New York", "state": "NY", "pin": "10001"}

addrress1 = Address(**address_dict)
patient_dict = {"name": "Alice","age": 30,  "gender": "Female","address": address_dict }

patient1 = Patient(**patient_dict)

print(patient1)
print(patient1.address.city)
print(patient1.address.state)