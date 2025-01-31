from typing import Optional

from fastapi import Depends, Request
from fastapi_users import (BaseUserManager, IntegerIDMixin, exceptions, models,
                           schemas)

from auth.models import User
from auth.utils import get_user_db
from config import SECRET_AUTH
from sqlalchemy.ext.asyncio import AsyncSession
from cart.models import cart
from database import get_async_session
class UserManager(IntegerIDMixin, BaseUserManager[User, int]):
    reset_password_token_secret = SECRET_AUTH
    verification_token_secret = SECRET_AUTH

    async def on_after_register(self, user: User, request: Optional[Request] = None):
        print(f"User {user.id} has registered.")

    async def create(
        self,
        user_create: schemas.UC,
        safe: bool = False,
        request: Optional[Request] = None,
    ) -> models.UP:
        await self.validate_password(user_create.password, user_create)

        existing_user = await self.user_db.get_by_email(user_create.email)
        if existing_user is not None:
            raise exceptions.UserAlreadyExists()

        user_dict = (
            user_create.create_update_dict()
            if safe
            else user_create.create_update_dict_superuser()
        )
        password = user_dict.pop("password")
        user_dict["hashed_password"] = self.password_helper.hash(password)
      

        created_user = await self.user_db.create(user_dict)

        await self.on_after_register(created_user, request)

        return created_user


async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)
async def add_to_cart(session: AsyncSession, user_id: int, quantity: int):
    new_cart_item = cart(user_id=user_id, items=quantity)
    
    session.add(new_cart_item)
    await session.commit()  # Зафиксировать изменения в БД
    await session.refresh(new_cart_item)  # Обновить объект с добавленным ID
    
    return new_cart_item