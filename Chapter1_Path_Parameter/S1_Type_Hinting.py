
# Type hinting means telling Python what type of data a variable, 
#      function parameter, or return value should be.

from fastapi import FastAPI
from typing import Any

text:str = "Name"    # text is expected to be a string
number:int = 10
pi:float = 3.14


num: int | float = 10

def root(value: int | float) -> float:  # The function is expected to return a float
    return value ** 0.5

root_value = root(25)
print(f"Root value: {root_value}")

shipping: dict[str, int | float | str] = {
    "name": "Package A",
    "weight": 10.5, 
    "length": 20,
    "width": 15
}

shipping2: dict[str, Any] = {
    "name": "Package A",
    "weight": 10.5, 
    "length": 20,
    "width": 15
}

table : tuple[int, ...] = (10, 20, 30, 40)
lst : list[int | str] = [10, "Hello", 20, "World"]


temp : int | None
temp = 10




# 🚀 Why type hinting is CRITICAL in FastAPI

# FastAPI uses type hints to automatically:

# ✅ Validate request data
# ✅ Convert data types
# ✅ Generate API documentation (Swagger)
# ✅ Catch errors early
# ✅ Improve editor autocomplete

# Example:

app = FastAPI()
                                    # What happens here:
@app.get("/items/{item_id}")        # item_id: int
def read_item(item_id: int):        # If user sends /items/abc ❌
    return {"item_id": item_id}     # FastAPI returns 422 Validation Error automatically
                                    # 🔥No manual validation code needed