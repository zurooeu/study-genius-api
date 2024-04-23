from fastapi import FastAPI

from app.actions import process_query
from app.model import ConversationRequest

app = FastAPI()


@app.post("/conversation/")
async def post_conversation(conversation: ConversationRequest):
    await process_query(conversation)
    return {"conversation_id": conversation.conversation_id, "query": conversation.query}
