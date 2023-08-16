import os
from dotenv import load_dotenv

load_dotenv()

model_path = os.environ.get("MODEL_PATH")


def assert_compulsory_env():
    if model_path is None:
        raise Exception("Model Path is not set, please set it in the .env file")
