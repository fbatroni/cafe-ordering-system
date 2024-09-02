from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers.v1.users import users_router, users_admin_router
from app.routers.v1.orders import orders_router, orders_admin_router
from app.routers.v1.locations import locations_router, locations_admin_router
from app.routers.v1.menu_items import menu_items_router, menu_items_admin_router
from app.routers.v1.categories import categories_router, categories_admin_router

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

# customer routes
app.include_router(users_router)
app.include_router(orders_router)
app.include_router(menu_items_router)
app.include_router(categories_router)
app.include_router(locations_router)

# admin routes
app.include_router(users_admin_router)
app.include_router(orders_admin_router)
app.include_router(menu_items_admin_router)
app.include_router(categories_admin_router)
app.include_router(locations_admin_router)

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

