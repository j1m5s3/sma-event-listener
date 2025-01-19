import os, json
from dotenv import dotenv_values, find_dotenv

from utils.config_utils import select_enum_from_string
from utils.constants.contract_addresses import CONTRACTS
from utils.constants.enums import RPCEnv, ChainIds, RPCProviders, ConnectionTypes

ENV: str = os.environ.get('ENV', None)
if ENV is None:
    config: dict = dotenv_values(dotenv_path=find_dotenv('.env'))
else:
    config: dict = dotenv_values(dotenv_path=find_dotenv('.env.testnet'))

SMA_ADDRESS: str = os.environ.get('SMA_ADDRESS', None)

RPC_ENV: RPCEnv = select_enum_from_string(RPCEnv, config['RPC_ENV'])
CHAIN: ChainIds = select_enum_from_string(ChainIds, config['CHAIN'])
RPC_PROVIDER: RPCProviders = select_enum_from_string(RPCProviders, config['RPC_PROVIDER'])
RPC_CONNECTION_TYPE: ConnectionTypes = select_enum_from_string(ConnectionTypes, config['RPC_CONNECTION_TYPE'])

cur_dir = os.path.dirname(__file__)
rpc_url_json_fp: str = os.path.join(cur_dir, 'utils/constants/json_files/rpc_urls.json')
with open(rpc_url_json_fp, 'r') as f:
    rpc_urls: dict = json.load(f)

RPC_URL: str = rpc_urls[CHAIN.name][RPC_PROVIDER.name][RPC_CONNECTION_TYPE.name.lower()]
CONTRACT_ADDRESSES: dict = CONTRACTS[RPC_ENV][CHAIN]

if __name__ == '__main__':
    print(f"ENV: {ENV}")
    print(f"RPC_ENV: {RPC_ENV}")
    print(f"CHAIN: {CHAIN}")
    print(f"RPC_PROVIDER: {RPC_PROVIDER}")
    print(f"RPC_CONNECTION_TYPE: {RPC_CONNECTION_TYPE}")
    print(f"RPC_URL: {RPC_URL}")
    print(f"CONTRACT_ADDRESSES: {CONTRACT_ADDRESSES}")
    print(f"SMA_ADDRESS: {SMA_ADDRESS}")