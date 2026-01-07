
from pydantic import BaseModel, Field

# ===== PYDANTIC MODEL NOTES =====

# 1. WHAT IS PYDANTIC?
# Pydantic is a Python library for data validation and settings management
# It uses Python type annotations to validate data at runtime
# Provides clear and helpful error messages when validation fails

# 2. KEY FEATURES
# - Data validation using Python type hints
# - Automatic type coercion/conversion
# - JSON schema generation
# - Works seamlessly with FastAPI
# - Supports complex nested models
# - IDE autocompletion support

# 3. BASIC USAGE
# from pydantic import BaseModel
# 
# class User(BaseModel):
#     name: str
#     age: int
#     email: str

# 4. TYPE VALIDATION
# - Automatically validates types (str, int, float, bool, etc.)
# - Raises ValidationError if data doesn't match type
# - Supports Optional[T] for optional fields
# - Can set default values

# 5. FIELD CONSTRAINTS
# - Use Field() for advanced validation
# - Can set: min_length, max_length, regex, gt, lt, ge, le
# - Example: age: int = Field(..., gt=0, lt=150)

# 6. NESTED MODELS
# - Models can contain other models
# - Supports lists and dictionaries
# - Enables complex data structures

# 7. CONFIGURATION
# - Use Config class inside model
# - Can set: json_encoders, allow_population_by_field_name, etc.

# 8. COMMON METHODS
# - model_validate() - Create model from dict
# - model_dump() - Convert to dictionary
# - model_dump_json() - Convert to JSON string
# - schema() - Get JSON schema

# 9. ERROR HANDLING
# - Catches validation errors before processing
# - Provides detailed error messages
# - Helps maintain data integrity

# 10. FASTAPI INTEGRATION
# - Automatic request body validation
# - Automatic response serialization
# - Interactive API documentation (Swagger UI)


class Shipment(BaseModel):
    content: str = Field(
        description="Contents of the shipment",
        # max length of characters
        max_length=30,
        # can use min length as well
        min_length=8,
    )
    weight: float = Field(
        description="Weight of the shipment in kilograms (kg)",
        # [l]ess than or [e]qual to
        le=25,
        # [g]reater than or [e]qual to
        ge=1,
    )
    destination: int | None = Field(
        description="Destination Zipcode. If not provided will be sent off to a random location",
        # fixed default value
        default=11000,
        # or generate at runtime using default_factory
        # here a random integer 
        # default_factory=lambda : randint(11000, 11999),
    )
