from typing import Any
"""
Query Parameters: are optional key-value pairs appended to the end or the URL, used to pass additional information to the server.
in an HTTP request. They are typically used for filtering, sorting, pagination, 
and other operations that modify the response without changing the resource being accessed.

Example: In the URL `http://example.com/items?category=books&sort=price_asc`, `category` and `sort` are query parameters.
"""

from fastapi import FastAPI


app = FastAPI()

shipments = {
    12701: {"weight": 0.6, "content": "glassware", "status": "placed"},
    12702: {"weight": 2.3, "content": "books", "status": "shipped"},
    12703: {"weight": 1.1, "content": "electronics", "status": "delivered"},
    12704: {"weight": 3.5, "content": "furniture", "status": "in transit"},
    12705: {"weight": 0.9, "content": "clothing", "status": "returned"},
}

# Use path and query parameters together
@app.get("/shipment/{field}")
def get_shipment_field(field: str, id: int) -> Any:
    return shipments[id][field]