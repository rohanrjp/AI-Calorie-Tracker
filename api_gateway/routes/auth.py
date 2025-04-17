from fastapi import APIRouter,status
from services.auth_services.auth_schemas import UserSignUp

auth_router=APIRouter(prefix="/auth",tags=["Auth"])

@auth_router.post("/sign-up",status_code=status.HTTP_201_CREATED)
async def user_sign_up(new_user:UserSignUp):
    return {"message":f"{new_user.email} , {new_user.name}, {new_user.password}"}