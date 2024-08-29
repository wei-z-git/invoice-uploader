import os
from dotenv import load_dotenv, find_dotenv
from pydantic_settings import BaseSettings
from typing import List


class Config(BaseSettings):
    # load environment variables
    load_dotenv(find_dotenv(), verbose=True, override=True)
    ROOT_PATH: str = "/"
    GITEE_ACCESS_TOKEN: str = ""


settings = Config()
