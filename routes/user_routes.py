from database.pydantic_models import SignupModel, LoginModel
from fastapi import HTTPException, APIRouter, Depends, Query
from tortoise.exceptions import DoesNotExist, IntegrityError
from database.models import User, Role, Roles
from utils.helper import hash_password

user_router = APIRouter()

@user_router.get("/roles")
async def get_all_roles():
    res  = await Role.all()
    return res

@user_router.post("/signup")
async def signup(request: SignupModel):
    email= request.email.lower()

    if await User.filter(email=email).exists():
        raise HTTPException(status_code=400, detail="Email already exists")

    role = await Role.get(role_name=Roles.USER)
    try:
        user = await User.create(
            email=email,
            password=hash_password(request.password),
            name=request.name,
            role=role
        )
    except IntegrityError:
        raise HTTPException(status_code=400, detail="Email already exists")

    return {
        "id": user.id,
        "email": user.email,
        "name": user.name,
        "role": user.role.role_name
    }


@user_router.post("/login")
async def login(request: LoginModel):
    email = request.email.lower()
    password = request.password

    # pass = hash_password(request.password)