# Pydantic Crash Course

A comprehensive collection of Python scripts demonstrating the key features and capabilities of Pydantic, a powerful data validation and parsing library for Python.

## Table of Contents

- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Examples](#examples)
- [Running the Examples](#running-the-examples)
- [Contributing](#contributing)
- [License](#license)

## Overview

This repository contains practical examples that cover the fundamental concepts of Pydantic, including:

- Basic model definition and validation
- Field validators for custom validation logic
- Model validators for cross-field validation
- Computed fields for derived properties
- Nested models for complex data structures
- Serialization and deserialization
- Type annotations and field constraints

Each script is self-contained and includes comments explaining the concepts being demonstrated.

## Prerequisites

- Python 3.8 or higher
- Basic understanding of Python classes and type hints

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/pydantic-crash-course.git
   cd pydantic-crash-course
   ```

2. Install Pydantic:
   ```bash
   pip install pydantic
   ```

## Examples

### 1. `why_pydantic.py`
Introduces the problems that Pydantic solves, such as type checking and data validation in traditional Python functions. Explains Pydantic's three-step process: define a model, create an instance, and use validated data.

### 2. `pydantic_apply.py`
Demonstrates basic Pydantic model creation with various field types, including optional fields, field constraints, and type annotations using `Annotated`.

### 3. `field_validator.py`
Shows how to use field validators to perform custom validation on individual fields. Covers both 'before' and 'after' validation modes, with examples of email domain validation, name transformation, and age range checking.

### 4. `model_validator.py`
Illustrates model validators for cross-field validation. Demonstrates validating relationships between multiple fields, such as requiring emergency contact information for elderly patients.

### 5. `computed_fields.py`
Explains computed fields (properties calculated from other fields). Includes an example of calculating BMI from weight and height.

### 6. `nested_models.py`
Covers nested models for representing complex, hierarchical data structures. Shows how to define and use nested Pydantic models like Address within a Patient model.

### 7. `serialization.py`
Demonstrates Pydantic's serialization capabilities, including converting model instances to JSON strings and Python dictionaries using `model_dump_json()` and `model_dump()`.

## Running the Examples

Each Python script can be run independently. For example:

```bash
python why_pydantic.py
python pydantic_apply.py
python field_validator.py
python model_validator.py
python computed_fields.py
python nested_models.py
python serialization.py
```

The scripts will output validation results, error messages (where applicable), and demonstrate the Pydantic features in action.

## Key Concepts Covered

- **BaseModel**: The foundation class for all Pydantic models
- **Field Types**: Standard Python types enhanced with validation
- **Field Validators**: Custom validation logic for individual fields
- **Model Validators**: Validation logic that considers multiple fields
- **Computed Fields**: Properties calculated from other model data
- **Nested Models**: Models containing other models
- **Serialization**: Converting models to different formats
- **Type Annotations**: Using `typing` module for complex types
- **Field Constraints**: Setting limits and requirements on field values

## Contributing

Contributions are welcome! If you'd like to add more examples, improve existing code, or fix issues:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add or update tests if necessary
5. Submit a pull request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Resources

- [Pydantic Official Documentation](https://docs.pydantic.dev/)
- [Pydantic GitHub Repository](https://github.com/pydantic/pydantic)
- [Python Typing Documentation](https://docs.python.org/3/library/typing.html)

---

Happy validating with Pydantic! 🚀