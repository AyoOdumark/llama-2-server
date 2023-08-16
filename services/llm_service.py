import datetime
from llama_cpp import Llama
from db.store import insert_chat
from config import model_path

from type import DbChatItem


def completion(chats):
    print(chats)
    llm = Llama(
        model_path=model_path,
        n_ctx=2048,
    )

    messages = [
        {"role": "system", "content": "You are my personal assistant. I know nothing"},
    ]

    session_id = ""
    for message in chats:
        session_id = message[0]
        new_message_dict = {"role": message[1], "content": message[3]}
        messages.append(new_message_dict)

    print(messages)

    output = llm.create_chat_completion(
        messages=messages,
        temperature=0.5,
        top_p=0.8,
        top_k=50,
        stream=False,
        stop=["### Assistant:", "### Human:"],
        max_tokens=150,
        repeat_penalty=1.2,
        presence_penalty=0.2,
    )

    system_response = output["choices"][0]["message"]["content"]

    insert_chat(
        DbChatItem(
            session_id=session_id,
            date=datetime.datetime.now(),
            role="assistant",
            message=system_response,
        )
    )

    return system_response
