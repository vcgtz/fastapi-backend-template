from fastapi import APIRouter

from .controller import UserController

router = APIRouter(
    prefix="/users",
    tags=["users"],
)


@router.get("/")
async def get_all_users():
    return UserController.get_all_users()


@router.get("/{user_id}")
async def get_user(user_id: int):
    return UserController.get_user(user_id)


@router.post("/")
async def store_user():
    return UserController.store_user({})


@router.put("/{user_id}")
async def update_user(user_id: int):
    return UserController.update_user(user_id)


@router.delete("/{user_id}")
async def delete_user(user_id: int):
    return UserController.delete_user(user_id)
