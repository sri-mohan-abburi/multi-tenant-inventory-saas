# Multi-Tenant SaaS Inventory Platform 📦

**Architecture:** Monolithic Async API with Logical Tenant Isolation
**Status:** Active Development

## 🚀 Project Overview
This project is a high-performance **Software-as-a-Service (SaaS)** platform designed to manage inventory, orders, and fulfillment for multiple independent organizations (tenants). It utilizes **PostgreSQL Row-Level Security (RLS)** to ensure strict data isolation while sharing a single database instance—a pattern commonly used for cost-effective scaling on AWS.

## 🏗 System Architecture
* **API Layer:** FastAPI (Python 3.14) for non-blocking I/O.
* **Database:** PostgreSQL with **SQLAlchemy** (Async) and **Alembic** for migrations.
* **Security:** OAuth2 with JWT tokens containing tenant context (Schema Isolation).
* **Infrastructure:** Designed for AWS Lambda/Fargate deployment via Docker.

## 🛠 Features (Planned)
* **Multi-Tenancy:** Single database, shared schema, logical isolation via `tenant_id`.
* **RBAC:** Role-Based Access Control (Admin vs. Staff vs. Viewer).
* **Inventory Engine:** Real-time stock tracking with audit logs.
* **Order Management:** ACID-compliant transaction processing for orders.

## ⚡ Tech Stack
* **Language:** Python 3.14
* **Framework:** FastAPI
* **Data Validation:** Pydantic V2
* **ORM:** SQLAlchemy 2.0 (Async)
* **Migrations:** Alembic