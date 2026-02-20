from pydantic import BaseModel , computed_field

class Patient(BaseModel):
    name: str
    age: int
    email: str
    weight: float
    height: float
    married: bool
    allergies: list[str] = []
    contact_details : dict[str, str] = {}

    @computed_field
    @property
    def bmi(self) -> float:
        return self.weight / (self.height / 100) ** 2  # BMI = weight (kg) / (height (m))^2

def insert_into_db(patient: Patient):
    print(patient.bmi)  # This will compute the BMI on the fly when we access it
    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.weight)
    print(patient.height)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print("Database insertion complete.")

# Example usage
patient_info = {'name': 'Prashant', 'age': 25, 'email': 'prashant@gmail.com', 'weight': 70.5, 'height': 175.0, 'married': True, 'allergies': ['pollen', 'dust'], 'contact_details': {'phone': '123-456-7890', 'address': '123 Main St'}}
patient1 = Patient(**patient_info)  # This will validate the data and create a Patient instance
insert_into_db(patient1)    