from pydantic import BaseModel , EmailStr , AnyUrl , Field , field_validator , model_validator

from typing import List , Dict , Optional , Annotated

class Patient(BaseModel):
    name: str 
    age: int
    email: EmailStr  # This will validate that the email is in a proper format
    weight : float
    married: bool
    allergies: Optional[List[str]] = []  # Optional field with a default value of an empty list
    contact_details : Optional[Dict[str, str]] = {} 
    
    @model_validator(mode='after')
    def validate_emergency_contact(cls, model):
        if model.age > 60 and 'emergency_contact' not in model.contact_details:
            raise ValueError("Emergency contact is required for patients over 60 years old")
        return model
    

def insert_into_db(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print("Database insertion complete.")

# Example usage
patient_info = {'name': 'Prashant', 'age': 89, 'email': 'prashant@icici.com', 'weight': 70.5, 'married': True, 'allergies': ['pollen', 'dust'], 'contact_details': {'emergency_contact': '123-456-7890', 'address': '123 Main St'}}
patient1 = Patient(**patient_info)  # This will validate the data and create a Patient instance
insert_into_db(patient1)    