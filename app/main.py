from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.api.v1.endpoints import tenants

from app.api.v1.endpoints import tenants, login


app = FastAPI(
    title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

app.include_router(tenants.router, prefix=settings.API_V1_TENANT_STR, tags=["tenants"])
app.include_router(login.router, prefix="/api/v1/login", tags=["Login"])

# CORS Middleware
# Critical for SaaS: Allows your future React/Next.js frontend to talk to this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
async def health_check():
    return {"status": "healthy", "version": "0.1.0"}


@app.get("/")
async def root():
    return {"message": "Welcome to the Multi-Tenant Inventory SaaS API!"}
