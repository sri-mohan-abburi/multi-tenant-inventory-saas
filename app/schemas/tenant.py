from pydantic import BaseModel, ConfigDict


class TenantBase(BaseModel):
    name: str
    schema_name: str


class TenantCreate(TenantBase):
    pass


class TenantResponse(TenantBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
