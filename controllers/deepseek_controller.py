import os
from dotenv import load_dotenv
from fastapi import APIRouter

from models.requests.prompt_request import PromptRequest
from models.responses.deepseek_chat_response import DeepSeekChatResponse
from openai import OpenAI

router = APIRouter()

load_dotenv()  # Load environment variables from .env file

client = OpenAI(api_key=os.getenv("DEEPSEEK_API_KEY"), base_url="https://api.deepseek.com")


@router.post("/", response_model=DeepSeekChatResponse)
async def chat(prompt_request: PromptRequest):
   
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content": prompt_request.prompt},
        ],
        stream=False
    )

    #print(response.choices[0].message.content)

    return {
        "output": response.choices[0].message.content
    }