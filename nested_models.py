from pydantic import BaseModel

class Address(BaseModel):
    street: str
    city: str
    state: str
    zip_code: str

class Patient(BaseModel):
    name: str
    age: int
    email: str
    weight: float
    married: bool
    address: Address
    allergies: list[str] = []
    contact_details : dict[str, str] = {}

def insert_into_db(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.weight)
    print(patient.married)
    print(patient.address.street)
    print(patient.address.city)
    print(patient.address.state)
    print(patient.address.zip_code)
    print(patient.allergies)
    print(patient.contact_details)
    print("Database insertion complete.")

# Example usage 
address_info = {'street': '123 Main St', 'city': 'Anytown', 'state': 'Anystate', 'zip_code': '12345'}
address1 = Address(**address_info)  # This will validate the address data and create an Address instance
patient_info = {'name': 'Prashant', 'age': 25, 'email': 'prashant@gmail.com', 'weight': 70.5, 'married': True, 'address': address_info, 'allergies': ['pollen', 'dust'], 'contact_details': {'phone': '123-456-7890', 'occupation': 'Software Engineer'}}
patient1 = Patient(**patient_info)  # This will validate the patient data and create a Patient instance
insert_into_db(patient1)