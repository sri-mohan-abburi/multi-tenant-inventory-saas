from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer, Float
from app.db.base_class import Base, TenantMixin


class Product(Base, TenantMixin):
    # TenantMixin automatically adds 'tenant_id'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    sku: Mapped[str] = mapped_column(String, index=True)  # Stock Keeping Unit
    name: Mapped[str] = mapped_column(String, index=True)
    description: Mapped[str] = mapped_column(String, nullable=True)
    price: Mapped[float] = mapped_column(Float, default=0.0)
