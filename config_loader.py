import os
from dotenv import dotenv_values, find_dotenv

ENV: str = os.environ.get('ENV', None)
if ENV is None:
    config: dict = dotenv_values(dotenv_path=find_dotenv('.env'))
else:
    config: dict = dotenv_values(dotenv_path=find_dotenv('.env.testnet'))

SMA_ADDRESS: str = os.environ.get('SMA_ADDRESS', None)

