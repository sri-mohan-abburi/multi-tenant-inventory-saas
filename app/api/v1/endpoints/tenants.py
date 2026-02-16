from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.api import deps
from app.schemas.tenant import TenantCreate, TenantResponse
from app.schemas.user import UserCreate, UserResponse
from app.crud import crud_tenant, crud_user

router = APIRouter()

# Schema for the combined request
from pydantic import BaseModel


class TenantSignupRequest(BaseModel):
    tenant: TenantCreate
    user: UserCreate


@router.post("/signup", status_code=status.HTTP_201_CREATED)
async def regoster_tenant(
    signup_data: TenantSignupRequest, db: AsyncSession = Depends(deps.get_db)
):
    """
    Onboard a new tenant with an admin user.
    """
    # 1. check if tenant exists
    tenant_exists = await crud_tenant.get_tenant_by_schema(
        db, schema_name=signup_data.tenant.schema_name
    )
    if tenant_exists:
        raise HTTPException(
            status_code=400, detail="Tenant with this schema name already exists."
        )

    # 2. check if user email exists
    user_exists = await crud_user.get_user_by_email(db, email=signup_data.user.email)
    if user_exists:
        raise HTTPException(
            status_code=400, detail="User with this email already exists."
        )

    # 3. create tenant
    new_tenant = await crud_tenant.create_tenant(db, signup_data.tenant)

    # 4. create admin user for the tenant
    new_user = await crud_user.create_user(
        db, user_in=signup_data.user, tenant_id=new_tenant.id
    )

    return {
        "status": "created",
        "tenant_id": new_tenant.id,
        "admin_email": new_user.email,
    }
