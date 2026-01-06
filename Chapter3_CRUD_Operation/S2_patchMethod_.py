from typing import Any, Optional

from fastapi import FastAPI, HTTPException, status
from scalar_fastapi import get_scalar_api_reference


app = FastAPI()

shipments = {
    12701: {"weight": 0.6, "content": "glassware", "status": "placed"},
    12702: {"weight": 2.3, "content": "books", "status": "shipped"},
    12703: {"weight": 1.1, "content": "electronics", "status": "delivered"},
    12704: {"weight": 3.5, "content": "furniture", "status": "in transit"},
    12705: {"weight": 0.9, "content": "clothing", "status": "returned"},
    12706: {"weight": 4.0, "content": "appliances", "status": "processing"},
    12707: {"weight": 1.8, "content": "toys", "status": "placed"},
}


# Update shipment details (using PATCH)  -> Update only specific fields of a shipment
@app.patch("/shipment")
def patch_shipment(
    id: int,
    content: Optional[str] = None,
    weight: Optional[float] = None,
    status: Optional[str] = None,
) -> dict[str, Any]:
    # Get current shipment details
    current_shipment = shipments[id]
    # Update only the fields that are provided
    if content is not None:
        current_shipment["content"] = content
    if weight is not None:
        current_shipment["weight"] = weight
    if status is not None:
        current_shipment["status"] = status
    shipments[id] = current_shipment
    return current_shipment


# Scalar API Documentation
@app.get("/scalar", include_in_schema=False)
def get_scalar_docs():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title="Scalar API",
    )
