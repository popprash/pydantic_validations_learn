from pydantic import BaseModel , EmailStr , AnyUrl , Field
from typing import List , Dict , Optional , Annotated

class Patient(BaseModel):
    linkln: Optional[AnyUrl] = None  # Optional field for LinkedIn profile URL
    name: str = Annotated[str,Field( max_length=100, description="Patient's full name", title="Full Name" , example="John Doe")]  # Required field with a maximum length of 100
    email: EmailStr  # This will validate that the email is in a proper format
    age: int
    weight: Optional[float] = Field(gt=0, lt=100, strict=True) #  Strictly greater than 0 and less than 100, and must be a float (not an integer)
    married: Annotated[bool, Field(default=False , description="Whether the patient is married or not ")] = False  # Optional field with a default value of False
    allergies: Optional[List[str]] = []  # Optional field with a default value of an empty list
    contact_details : Optional[Dict[str, str]] = {}  # Optional field with a default value of an empty dictionary 

def insert_into_db(patient: Patient):
    # Imagine this function inserts data into a database
    print(f"Inserting {patient.name}, age {patient.age} into the database...")
    print(f"Weight: {patient.weight}, Married: {patient.married}, Allergies: {patient.allergies}, Contact Details: {patient.contact_details}") 
    print("Database insertion complete.")
    

# Example usage
patient_info = {'name': 'Prashant', 'age': 25, 'email': 'prashant@example.com', 'weight': 70.5, 'married': True, 'allergies': ['nuts', 'dust'], 'contact_details': {'email': 'prashant@example.com', 'phone': '123-456-7890'}}  # This will cause a validation error because 'age' is not an integer when there is a typo in the key, but Pydantic will catch this error and raise a ValidationError.
patient1 = Patient(**patient_info)  # This will validate the data and create a Patient instance

insert_into_db(patient1)