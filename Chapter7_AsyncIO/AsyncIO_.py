from fastapi import FastAPI
import asyncio
import httpx

"""
AsyncIO in FastAPI
==================

AsyncIO is Python's built-in library for writing asynchronous code using async/await syntax.
FastAPI is built on top of Starlette, which fully supports AsyncIO, allowing you to write
non-blocking, concurrent code that can handle multiple requests efficiently.

Key Benefits:
- Handle multiple requests concurrently without threads
- Better performance for I/O-bound operations (database calls, HTTP requests)
- Cleaner syntax compared to callbacks or threading
- Native integration with FastAPI

Example:
--------
"""


app = FastAPI()


# Example 1: Simple async route
@app.get("/hello")
async def hello():
    """Async endpoint that returns a greeting"""
    await asyncio.sleep(1)  # Simulates I/O operation
    return {"message": "Hello, World!"}


# Example 2: Async database operation
@app.get("/users/{user_id}")
async def get_user(user_id: int):
    """Async endpoint that simulates fetching from database"""
    await asyncio.sleep(0.5)  # Simulates DB query
    return {"user_id": user_id, "name": "John Doe"}


# Example 3: Async external API call
@app.get("/fetch-data")
async def fetch_external_data():
    """Async endpoint that calls external API"""
    async with httpx.AsyncClient() as client:
        response = await client.get("https://jsonplaceholder.typicode.com/posts/1")
        return response.json()


# Example 4: Multiple concurrent operations
@app.get("/concurrent")
async def concurrent_operations():
    """Execute multiple async operations concurrently"""
    results = await asyncio.gather(
        asyncio.sleep(1),
        asyncio.sleep(1),
        asyncio.sleep(1),
    )
    return {"message": "All operations completed concurrently"}