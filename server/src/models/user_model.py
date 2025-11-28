from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    email: str

class UserRead(BaseModel):
    id: int
    name: str
    email: str
    department:str
    roles:str
    

class UserUpdate(BaseModel):
    name: str | None = None
    email: str | None = None
