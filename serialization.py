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


# Example usage 
address_info = {'street': '123 Main St', 'city': 'Anytown', 'state': 'Anystate', 'zip_code': '12345'}
address1 = Address(**address_info)  # This will validate the address data and create an Address instance
patient_info = {'name': 'Prashant', 'age': 25, 'email': 'prashant@gmail.com', 'weight': 70.5, 'married': True, 'address': address_info, 'allergies': ['pollen', 'dust'], 'contact_details': {'phone': '123-456-7890', 'occupation': 'Software Engineer'}}
patient1 = Patient(**patient_info)  # This will validate the patient data and create a Patient instance
# insert_into_db(patient1)
temp = patient1.model_dump_json()  # This will serialize the patient data to a JSON string
print(temp)
print(type(temp))

temp2 = patient1.model_dump()  # This will serialize the patient data to a Python dictionary
print(temp2)
print(type(temp2))  

temp3 = patient1.model_dump(include={'name', 'age', 'email'})  # This will serialize only the specified fields to a Python dictionary
print(temp3)    
temp4 = patient1.model_dump(exclude={'allergies', 'contact_details'})  # This will serialize all fields except the specified ones to a Python dictionary
print(temp4)        
# exclued_unset = True will exclude all the fields that are not set in the model, so if we have any optional fields that are not set, they will be excluded from the serialization output.
temp5 = patient1.model_dump(exclude_unset=True)  # This will serialize only the fields that are set in the model to a Python dictionary
print(temp5)