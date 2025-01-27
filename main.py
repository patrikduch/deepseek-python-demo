from controllers import deepseek_controller
from dotenv import load_dotenv
from fastapi import FastAPI



app = FastAPI()

load_dotenv()  # Load environment variables from .env file


# Include routers from different controllers
app.include_router(deepseek_controller.router, prefix="/api/deepseek", tags=["DeepSeek"])