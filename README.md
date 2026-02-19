# Multi-Tenant SaaS Inventory Platform

**Architecture:** Monolithic Async API with Row-Level Tenant Isolation
**Status:** Production-Ready MVP

## Project Overview
This is a high-performance **Software-as-a-Service (SaaS)** platform designed to manage inventory for multiple independent organizations. It utilizes **PostgreSQL** with a Shared-Schema strategy to ensure strict data isolation while maintaining cost efficiency.

## System Architecture

* **API Layer:** FastAPI (Python 3.12) with Async SQLAlchemy.
* **Authentication:** OAuth2 with JWT (JSON Web Tokens).
* **Multi-Tenancy:** Logic-based isolation via `TenantMixin` (auto-injects `tenant_id`).
* **Infrastructure:** Dockerized Database & Application.

## Key Features
* **Tenant Onboarding:** `POST /signup` creates a Tenant Organization + Admin User in one transaction.
* **Secure Login:** Stateless JWT authentication with BCrypt password hashing.
* **Inventory Management:** CRUD operations for Products, strictly scoped to the logged-in user's tenant.
* **Async Database:** High-concurrency support using `asyncpg` drivers.

## How to Run
1.  **Clone the Repo:**
    ```bash
    git clone [https://github.com/sri-mohan-abburi/Multi-Tenant-SaaS-Inventory-Platform.git](https://github.com/sri-mohan-abburi/Multi-Tenant-SaaS-Inventory-Platform.git)
    cd Multi-Tenant-SaaS-Inventory-Platform
    ```

2.  **Start Infrastructure:**
    ```bash
    docker-compose up -d
    ```

3.  **Run Migrations:**
    ```bash
    alembic upgrade head
    ```

4.  **Start API:**
    ```bash
    uvicorn app.main:app --reload
    ```

## API Usage
* **Swagger UI:** `http://localhost:8000/docs`
* **Workflow:**
    1.  **Signup:** Create a new Tenant (e.g., "Tesla").
    2.  **Login:** Get a Bearer Token.
    3.  **Manage:** Use Token to add Products (e.g., "Model S").