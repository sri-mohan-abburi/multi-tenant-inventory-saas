from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.tenant import Tenant
from app.schemas.tenant import TenantCreate


async def create_tenant(db: AsyncSession, tenant_in: TenantCreate) -> Tenant:
    db.obj = Tenant(name=tenant_in.name, schema_name=tenant_in.schema_name)
    db.add(db.obj)
    await db.commit()
    await db.refresh(db.obj)
    return db.obj


async def get_tenant_by_schema(db: AsyncSession, schema_name: str) -> Tenant | None:
    query = select(Tenant).where(Tenant.schema_name == schema_name)
    result = await db.execute(query)
    return result.scalars().first()
