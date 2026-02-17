from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "Multi-Tenant Inventory SaaS"
    API_V1_STR: str = "/api/v1"
    API_V1_TENANT_STR: str = "/api/v1/tenants"

    # Security
    SECRET_KEY: str = "supersecretkey123"  # Will be loaded from .env in production
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # Database (Placeholder for now)
    POSTGRES_SERVER: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    SQLALCHEMY_DATABASE_URI: str

    class Config:
        case_sensitive = True
        env_file = ".env"


settings = Settings()
