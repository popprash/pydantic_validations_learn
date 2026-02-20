def insert_into_db(name: str, age: int):
    # Imagine this function inserts data into a database
    if type(name) == str and type(age) == int:
        print(f"Inserting {name}, age {age} into the database...")
        print("Database insertion complete.")
    else:
        raise TypeError("Invalid input types")
    
    # In a real application, you would have more complex logic here, and you might not want to raise an error directly. Instead, you could log the error or handle it in a way that doesn't disrupt the user experience.

# Example usage
insert_into_db("Alice", 30)
insert_into_db("Bob", "thirty")  # This will cause a type error, but Python won't catch it at runtime without additional checks.
# To handle this, we can use Pydantic to validate the input data before inserting it into the database.

# Problems 
# 1. No type checking: The function relies on the caller to provide the correct types, which can lead to runtime errors if the wrong types are passed.
# 2. No data validation: The function does not validate the input data, so it could accept invalid data (e.g., negative ages, empty names).
# 3. No error handling: The function raises a TypeError if the input types are incorrect, but it does not provide a way to handle this error gracefully. In a real application, you would want to log the error or return a user-friendly message instead of crashing the program.

# Pydantic Works in 3 'steps:
# 1. Define a model: You create a class that inherits from BaseModel and define the fields with their types.

# 2. Create an instance: You create an instance of the model by passing the data to it. Pydantic will automatically validate the data and convert it to the correct types if possible.

# 3. Use the validated data: You can access the validated data through the model instance, and you can be confident that it is of the correct type and has passed any validation checks you have defined. This helps to prevent runtime errors and ensures that your application is working with clean, validated data.