import os
from dotenv import load_dotenv, find_dotenv
from pydantic_settings import BaseSettings
from typing import List


class Config(BaseSettings):
    # load environment variables
    load_dotenv(find_dotenv(), verbose=True, override=True)
    ROOT_PATH: str = "/"
    AKS_CLUSTER_NAME: str = "rtmc-btccndly-02"
    CLIENT_ID: str = "xxx"
    CLIENT_SECRET: str = "xxx"


settings = Config()
