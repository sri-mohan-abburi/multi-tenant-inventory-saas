from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.product import Product
from app.schemas.product import ProductCreate


async def create_product(
    db: AsyncSession, product_in: ProductCreate, tenant_id: int
) -> Product:
    db_obj = Product(
        **product_in.model_dump(), tenant_id=tenant_id  # the tenant_id from the token
    )
    db.add(db_obj)
    await db.commit()
    await db.refresh(db_obj)
    return db_obj


async def get_products_by_tenant(db: AsyncSession, tenant_id: int):
    # This ensures User A only sees User A's products
    query = select(Product).where(Product.tenant_id == tenant_id)
    result = await db.execute(query)
    return result.scalars().all()
