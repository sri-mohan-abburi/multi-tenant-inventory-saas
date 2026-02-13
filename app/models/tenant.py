from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.base_class import Base


class Tenant(Base):
    """
    Tenant model represents a client or organization using the SaaS application.
    """

    __tablename__ = "tenant"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, index=True)
    schema_name: Mapped[str] = mapped_column(String, unique=True, index=True)

    # Relationships to users
    users = relationship("User", back_populates="tenant", cascade="all, delete-orphan")
