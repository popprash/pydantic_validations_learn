# Field validators works in two modes:
# before # after
from pydantic import BaseModel , EmailStr , AnyUrl , Field , field_validator

from typing import List , Dict , Optional , Annotated

class Patient(BaseModel):
    name: str 
    age: int
    email: EmailStr  # This will validate that the email is in a proper format
    weight : float
    married: bool
    allergies: Optional[List[str]] = []  # Optional field with a default value of an empty list
    contact_details : Optional[Dict[str, str]] = {} 
    @field_validator('email')
    @classmethod
    def validate_email(cls, value):
        valid_domains = ['hdfc.com', 'icici.com']  # List of valid email domains
        # abc@gmail.com
        domain = value.split('@')[-1]  # Extract the domain from the email
        if domain not in valid_domains:
            raise ValueError(f"Email domain must be one of the following: {', '.join(valid_domains)}")
        return value
    
    @field_validator('name')
    @classmethod
    def transform_name(cls,value):
        return value.upper()  # Convert the name to uppercase before storing it in the model
    
    @field_validator('age', mode='after') # mode = after is by default, so we can omit it, but I am adding it here for clarity
    # when done (mode = before) The values in here are before the type coercion, so if we pass age as a string, it will be a string here, and we can validate it accordingly. If we pass age as an integer, it will be an integer here.
    @classmethod
    def validate_age(cls, value):
        if 0< value < 120:
            return value
        raise ValueError("Age must be between 0 and 120")
    
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
patient_info = {'name': 'Prashant', 'age': '25', 'email': 'prashant@icici.com', 'weight': 70.5, 'married': True, 'allergies': ['pollen', 'dust'], 'contact_details': {'phone': '123-456-7890', 'address': '123 Main St'}}
patient1 = Patient(**patient_info)  # This will validate the data and create a Patient instance
insert_into_db(patient1)