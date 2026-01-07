#serialization of Nested Pydantic Models: 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# You can easily serialize nested Pydantic models to dictionaries or JSON.
# This is particularly useful for data exchange, storage, or API responses. 
# Pydantic provides built-in methods to convert models to dictionaries or JSON strings, preserving the nested structure.
# e.g., using the .dict() method to convert a nested model to a dictionary, or the .json() method to convert it to a JSON string. 

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

# Serialize to dictionary
temp = patient1.model_dump()
print("Serialized to dictionary:", temp)
print(type(temp))

# Serialize to JSON
json_data = patient1.model_dump_json()  
print("Serialized to JSON:", json_data)
print(type(json_data))

# Serialize to dictionary using including nested models
partial_dict = patient1.model_dump(include=["name", "age"])
print("Partially Serialized to dictionary:", partial_dict)

# Serialize to dictionary using excluding nested models
excluded_dict = patient1.model_dump(exclude={"address"})    
print("Excluded Serialized to dictionary:", excluded_dict)
print("Address City from excluded dict:", excluded_dict.get("address"))  # Should be None