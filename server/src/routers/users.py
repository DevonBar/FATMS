from fastapi import APIRouter, Depends, HTTPException
from src.db.connection import get_connection
from src.db.queries.user_queries import (
    get_all_users
)
from src.models.user_model import  UserRead

router = APIRouter()

@router.get("/", response_model=list[UserRead])
def list_users(conn=Depends(get_connection)):
    users = get_all_users(conn)
    return [UserRead(id=u[0], name=u[1], email=u[2],department=u[3],roles=u[4]) for u in users]

# @router.get("/{user_id}", response_model=UserRead)
# def read_user(user_id: int, conn=Depends(get_connection)):
#     user = get_user_by_id(conn, user_id)
#     if not user:
#         raise HTTPException(status_code=404, detail="User not found")
#     return UserRead(id=user[0], name=user[1], email=user[2])

# @router.post("/", response_model=UserRead)
# def create_new_user(data: UserCreate, conn=Depends(get_connection)):
#     new_id = create_user(conn, data.name, data.email)
#     return UserRead(id=new_id, name=data.name, email=data.email)

# @router.put("/{user_id}", response_model=UserRead)
# def update_existing_user(user_id: int, data: UserUpdate, conn=Depends(get_connection)):
#     user = get_user_by_id(conn, user_id)
#     if not user:
#         raise HTTPException(status_code=404, detail="User not found")

#     updated_name = data.name if data.name else user[1]
#     updated_email = data.email if data.email else user[2]

#     update_user(conn, user_id, updated_name, updated_email)

#     return UserRead(id=user_id, name=updated_name, email=updated_email)

# @router.delete("/{user_id}")
# def delete_existing_user(user_id: int, conn=Depends(get_connection)):
#     rows = delete_user(conn, user_id)
#     if rows == 0:
#         raise HTTPException(status_code=404, detail="User not found")
#     return {"message": "User deleted successfully"}
