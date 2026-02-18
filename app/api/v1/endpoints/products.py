from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.api import deps
from app.schemas.product import ProductCreate, ProductResponse
from app.crud import crud_product
from app.models.user import User

router = APIRouter()


@router.post("/", response_model=ProductResponse)
async def create_item(
    item_in: ProductCreate,
    db: AsyncSession = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user),
):
    """
    Create a new product.
    The tenant_id is automatically pulled from the logged-in user.
    """
    return await crud_product.create_product(
        db=db, product_in=item_in, tenant_id=current_user.tenant_id
    )


@router.get("/", response_model=list[ProductResponse])
async def read_items(
    db: AsyncSession = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user),
):
    """
    List all products belonging to the current user's tenant.
    """
    return await crud_product.get_products_by_tenant(
        db, tenant_id=current_user.tenant_id
    )
