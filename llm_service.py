from llama_cpp import Llama

def completion(text):
    llm = Llama(model_path="", n_ctx=2048)
    output = llm(text, max_tokens=100, stop=["Q:", "\n"], echo=True)

    return output["choices"][0]["text"]

