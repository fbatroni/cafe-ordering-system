from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers.v1.users import users_router
from app.routers.v1.admin import admin_router
from fastapi.openapi.utils import get_openapi

# Custom OpenAPI configuration to include security schemes
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        title="Cafe Ordering System - API Documentation",
        version="1.0.0",
        description="This API provides the functionality to interact with our Cafe Ordering System",
        routes=app.routes,
    )

    # Define security scheme
    security_scheme = {
        "BearerAuth": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT",
        }
    }

    openapi_schema["components"]["securitySchemes"] = security_scheme

    # Apply security scheme to all routes
    for path in openapi_schema["paths"].values():
        for method in path.values():
            method["security"] = [{"BearerAuth": []}]

    app.openapi_schema = openapi_schema
    return app.openapi_schema

app = FastAPI()
app.include_router(users_router)
app.include_router(admin_router)

app.openapi = custom_openapi

# Allow React frontend to communicate with FastAPI backend
origins = ["http://www.cafeorders.com"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

