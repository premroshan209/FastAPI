from typing import Optional
from sqlmodel import SQLModel, Field, create_engine, Session, select

"""
SQLModel - Overview and Examples

SQLModel is a library that combines SQLAlchemy and Pydantic, allowing you to:
1. Define database models that are also valid Pydantic models
2. Use the same model for database operations and API validation
3. Reduce code duplication and improve type safety

Key Benefits:
- Single source of truth for data models
- Automatic validation using Pydantic
- Full SQLAlchemy ORM support
- Great integration with FastAPI
"""



# Example 1: Basic SQLModel Definition
class User(SQLModel, table=True):
    """
    User model that serves as both database table and API schema.
    
    Attributes:
        id: Primary key (auto-generated)
        name: User's full name (required)
        email: User's email address (required)
        age: User's age (optional)
    """
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    email: str
    age: Optional[int] = None


# Example 2: Creating Database Connection
"""
SQLModel uses SQLAlchemy under the hood for database operations.
This example shows basic setup with SQLite.
"""
sqlite_url = "sqlite:///database.db"
engine = create_engine(sqlite_url, echo=True)


# Example 3: CRUD Operations with SQLModel
def create_user(user: User):
    """Create a new user in the database"""
    with Session(engine) as session:
        session.add(user)
        session.commit()
        session.refresh(user)
        return user


def read_user(user_id: int):
    """Read a user by ID"""
    with Session(engine) as session:
        user = session.get(User, user_id)
        return user


def update_user(user_id: int, user_update: User):
    """Update an existing user"""
    with Session(engine) as session:
        user = session.get(User, user_id)
        if user:
            user.name = user_update.name
            user.email = user_update.email
            session.add(user)
            session.commit()
            session.refresh(user)
        return user


def delete_user(user_id: int):
    """Delete a user by ID"""
    with Session(engine) as session:
        user = session.get(User, user_id)
        if user:
            session.delete(user)
            session.commit()


# Example 4: Advanced Querying
def get_all_users():
    """Retrieve all users from database"""
    with Session(engine) as session:
        statement = select(User)
        users = session.exec(statement).all()
        return users


def find_user_by_email(email: str):
    """Find user by email address"""
    with Session(engine) as session:
        statement = select(User).where(User.email == email)
        user = session.exec(statement).first()
        return user