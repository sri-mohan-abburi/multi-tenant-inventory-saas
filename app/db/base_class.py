from typing import Any
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, Integer, ForeignKey


class Base(DeclarativeBase):
    """
    Base class for all database models.
    """

    id: Any
    __name__: str

    # Automatically generate table name from class name
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()


class TenantMixin:
    """
    Mixin to strictly enforce multi-tenancy.
    Every table that inherits this will automatically have a 'tenant_id'.
    """

    @declared_attr
    def tenant_id(cls) -> Mapped[int]:
        # This foreign key ensures data integrity.
        # On Delete Cascade: If a Tenant is deleted, all their data vanishes automatically.
        return mapped_column(
            ForeignKey("tenant.id", ondelete="CASCADE"), nullable=False, index=True
        )
