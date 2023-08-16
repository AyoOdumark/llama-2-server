import datetime
from config import assert_compulsory_env
from services.llm_service import completion
from fastapi import FastAPI, HTTPException, Request
from type import DbChatItem, Query
from db.store import get_chat, init as db_init, insert_chat

app = FastAPI(
    prefix="/api/llama/",
    tags=["llama"],
)

assert_compulsory_env()
db_init()


@app.post("/generate")
def generate(request: Request, query: Query):
    session_id = request.headers.get("session_id")
    if session_id is None:
        raise HTTPException(
            status_code=400,
            detail="session_id is complusory, but missing in headers. Just use any random string or  number in session_id",
        )
    insert_chat(
        DbChatItem(
            session_id=session_id,
            date=datetime.datetime.now(),
            role="user",
            message=query.message,
        )
    )
    chats = get_chat(session_id)
    output = completion(chats)
    return output
