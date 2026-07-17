# HELIX AI Shop

> Production-ready Machine Learning API for predicting customer purchase amount using FastAPI and CatBoost.

---

## Overview

HELIX AI Shop is an end-to-end Machine Learning API designed to estimate customer purchase amounts based on demographic, behavioral, and transactional features.

The project follows a production-oriented architecture with clear separation between:

- API Layer
- Service Layer
- Feature Engineering Layer
- Model Layer
- Configuration Layer

The application is built using FastAPI and follows software engineering best practices for maintainability, scalability, and deployment.

---

## Features

- FastAPI REST API
- CatBoost Regression Model
- Centralized Feature Engineering
- Singleton Resource Loader
- Environment-based Configuration
- Structured Logging
- Global Exception Handling
- Automatic OpenAPI Documentation
- Production-ready Architecture
- Type-safe Configuration
- Modular Codebase

---

## Project Structure

```
helix-ai-shop/
│
├── api/
│   ├── routers/
│   │   ├── health.py
│   │   └── predict.py
│   │
│   ├── config.py
│   ├── constants.py
│   ├── docs.py
│   ├── exceptions.py
│   ├── feature_engineering.py
│   ├── loader.py
│   ├── logger.py
│   ├── responses.py
│   ├── schemas.py
│   ├── services.py
│   └── main.py
│
├── artifacts/
│
├── notebooks/
│
├── training/
│
├── tests/
│
├── .env.example
├── requirements.txt
└── README.md
```

---

## Technology Stack

| Category | Technology |
|-----------|------------|
| Language | Python 3.12 |
| API | FastAPI |
| ML Model | CatBoost |
| Validation | Pydantic v2 |
| Configuration | pydantic-settings |
| Serialization | Joblib |
| Documentation | Swagger / ReDoc |

---

## Machine Learning Pipeline

```
Client

↓

FastAPI Router

↓

Prediction Service

↓

Feature Engineering

↓

CatBoost Model

↓

Prediction

↓

JSON Response
```

---

## Feature Engineering

The API performs automatic feature engineering before prediction.

Examples include:

- Date Features
- Cyclical Features
- Frequency Encoding
- Interaction Features
- Age Group Encoding
- Behavioral Features

All transformations are identical to the training pipeline.

---

## Configuration

Application settings are managed through environment variables.

Example:

```
APP_NAME=HELIX AI Shop API

HOST=0.0.0.0

PORT=8000

MODEL_PATH=artifacts/model.pkl
```

See:

```
.env.example
```

---

## API Endpoints

### Health Check

```
GET /health
```

Response

```json
{
    "status":"healthy"
}
```

---

### Prediction

```
POST /predict
```

Request

```json
{
  "Age":32,
  "Gender":"Male",
  "City":"Bandung",
  "Product_Category":"Electronics",
  "Payment_Method":"Credit Card",
  "Device_Type":"Mobile",
  "Session_Duration_Minutes":25,
  "Pages_Viewed":15,
  "Is_Returning_Customer":1,
  "Delivery_Time_Days":2,
  "Customer_Rating":5,
  "Transaction_Date":"2025-08-20"
}
```

Response

```json
{
    "predicted_purchase_amount":842.57
}
```

---

## Running Locally

Clone repository

```bash
git clone https://github.com/yourusername/helix-ai-shop.git
```

Install dependencies

```bash
pip install -r requirements.txt
```

Copy environment variables

```bash
cp .env.example .env
```

Run application

```bash
uvicorn api.main:app --reload
```

---

## Interactive Documentation

Swagger

```
http://localhost:8000/docs
```

ReDoc

```
http://localhost:8000/redoc
```

---

## Design Principles

The project follows several software engineering principles:

- Single Responsibility Principle
- Dependency Injection
- Layered Architecture
- Singleton Resource Management
- Environment-based Configuration
- Clean Separation of Concerns

---

## Future Improvements

- Authentication
- API Rate Limiting
- Redis Caching
- Monitoring
- Metrics
- Docker Deployment
- CI/CD Pipeline
- Model Versioning
- MLflow Integration

---

## Author

Hilmi Aji

Machine Learning Engineer | Data Scientist | Business Analytics

```