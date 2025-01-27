from controllers import deepseek_controller
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

app = FastAPI()

load_dotenv()  # Load environment variables from .env file

# Customize the OpenAPI Schema (Swagger UI)
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="DeepSeek Python Demo API",
        version="1.0.0",
        description="Demo API showing basic integration of Deepseek API",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi


# Include routers from different controllers
app.include_router(deepseek_controller.router, prefix="/api/deepseek", tags=["DeepSeek"])