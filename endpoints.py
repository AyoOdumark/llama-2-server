from llm_service import completion
from fastapi import FastAPI

app = FastAPI(
    prefix="/api/llama/",
    tags=["llama"],
)

@app.post("/generate")
def generate(text:str):
    output = completion(text)
    return output

