from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "Multi-Tenant Inventory SaaS"
    API_V1_STR: str = "/api/v1"

    # Security
    SECRET_KEY: str = "changethis"  # Will be loaded from .env in production
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # Database (Placeholder for now)
    # POSTGRES_SERVER: str = "localhost"
    # POSTGRES_USER: str = "postgres"
    # POSTGRES_PASSWORD: str = "password"
    # POSTGRES_DB: str = "saas_db"

    class Config:
        case_sensitive = True


settings = Settings()
