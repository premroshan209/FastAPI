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


@app.get("/shipment")
def get_shipment(id: int) -> dict[str, Any]:
    # Check for shipment with given id
    if id not in shipments:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Given id doesn't exist!"
        )

    return shipments[id]


@app.post("/shipment")
def submit_shipment(query_param: Any, req_body: dict[str, Any]) -> dict[str, int]:
    # Get query parameters as well
    print(f"\nQuery Param: {query_param}\n")
    # Extract fields from request body
    content = req_body["content"]
    weight = req_body["weight"]
    # Validate weight
    if weight > 25:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail="Maximum weight limit is 25 kgs",
        )
    # Create and assign shipment a new id
    new_id = max(shipments.keys()) + 1
    # Add to shipments dict
    shipments[new_id] = {
        "content": content,
        "weight": weight,
        "status": "placed",
    }
    # Return id for later use
    return {"id": new_id}


# Update shipment details (using PUT)  -> Update all content of a shipment
@app.put("/shipment")
def update_shipment(
    id: int, content: str, weight: float, status: str
) -> dict[str, Any]:
    shipments[id] = {
        "content": content,
        "weight": weight,
        "status": status,
    }
    return shipments[id]


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

#delete shipment
@app.delete("/shipment")
def delete_shipment(id: int):
    if id not in shipments:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Given id doesn't exist!"
        )
    del shipments[id]
    return {"message": "Shipment deleted successfully"}

# Scalar API Documentation
@app.get("/scalar", include_in_schema=False)
def get_scalar_docs():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title="Scalar API",
    )
