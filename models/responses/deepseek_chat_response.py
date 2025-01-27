from pydantic import BaseModel

class DeepSeekChatResponse(BaseModel):
    output: str