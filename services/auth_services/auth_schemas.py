from pydantic import BaseModel,EmailStr,Field

class UserSignUp(BaseModel):
    name: str=Field(min_length=2,max_length=20)
    email:EmailStr
    password:str=Field(min_length=5,max_length=50)