from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from app.core.config import settings
import sys

print(f"DEBUG: FastAPI is connecting to DB at: {settings.SQLALCHEMY_DATABASE_URI}")

if "postgres" not in settings.SQLALCHEMY_DATABASE_URI:
    print("CRITICAL ERROR: The Database URL does not contain 'postgres'.")
    sys.exit(1)


# Create the async engine
engine = create_async_engine(settings.SQLALCHEMY_DATABASE_URI, echo=True, future=True)

# Create sessionmaker factory
SessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    autocommit=False,
    autoflush=False,
    expire_on_commit=False,  # <--- THIS IS THE KEY FIX
)
