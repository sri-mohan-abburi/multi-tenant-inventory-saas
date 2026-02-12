from typing import AsyncGenerator
from app.db.session import AsyncSessionLocal


async def get_db() -> AsyncGenerator:
    """
    Dependency that provides a database session.
    This is used in API routes to interact with the database.
    It ensures that the session is properly closed after use.

    Dependency Injection for Database Sessions.

    Usage in an endpoint:
    def get_users(db: AsyncSession = Depends(get_db)):
        ...

    Benefits:
    1. Automatic connection cleanup (yield/finally)
    2. Easy to mock for unit tests
    """
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()
