from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer
from app.db.base_class import Base, TenantMixin


class User(Base, TenantMixin):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    email: Mapped[str] = mapped_column(String, unique=True, index=True)
    hashed_password: Mapped[str] = mapped_column(String)
    full_name: Mapped[str] = mapped_column(String, index=True, nullable=True)
    role: Mapped[str] = mapped_column(String, default="staff")  # admin, manager, staff

    # Back reference to tenant
    tenant = relationship("Tenant", back_populates="users")
