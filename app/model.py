from typing import Optional

from pydantic import BaseModel


class ConversationRequest(BaseModel):
    query: str
    conversation_id: Optional[str] = None
