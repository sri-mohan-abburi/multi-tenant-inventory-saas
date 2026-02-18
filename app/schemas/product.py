from pydantic import BaseModel, ConfigDict


class ProductBase(BaseModel):
    sku: str
    name: str
    description: str | None = None
    price: float


class ProductCreate(ProductBase):
    pass


class ProductResponse(ProductBase):
    id: int
    tenant_id: int
    model_config = ConfigDict(from_attributes=True)
