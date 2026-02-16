from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.user import User
from app.schemas.user import UserCreate
from app.core.security import get_password_hash


async def create_user(db: AsyncSession, user_in: UserCreate, tenant_id: int) -> User:
    db_obj = User(
        email=user_in.email,
        hashed_password=get_password_hash(user_in.password),
        full_name=user_in.full_name,
        role=user_in.role,
        tenant_id=tenant_id,  # Linking the user to the tenant
    )
    db.add(db_obj)
    await db.commit()
    await db.refresh(db_obj)
    return db_obj


async def get_user_by_email(db: AsyncSession, email: str) -> User | None:
    query = select(User).where(User.email == email)
    result = await db.execute(query)
    return result.scalars().first()
