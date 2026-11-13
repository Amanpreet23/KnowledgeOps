from pydantic import BaseModel, Field, EmailStr

class SignupModel(BaseModel):
    password: str = Field(min_length=8, max_length=255)
    email: EmailStr
    name: str

class LoginModel(BaseModel):
    email: EmailStr
    password: str


