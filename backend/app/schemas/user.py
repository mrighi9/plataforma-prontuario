from pydantic import BaseModel, EmailStr, Field


class UserBase(BaseModel):
    name: str
    email: EmailStr
    role: str = Field(..., max_length=1)          # 'A', 'M', etc.
    cpf: str  = Field(..., pattern=r'^\d{3}\.\d{3}\.\d{3}-\d{2}$')


class UserCreate(UserBase):
    password: str


class UserRead(UserBase):
    id: int

    model_config = {"from_attributes": True}      # substitui orm_mode=True


class UserLogin(BaseModel):
    email: EmailStr
    password: str
