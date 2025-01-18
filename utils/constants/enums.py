from enum import Enum

class ConfiguredContracts(Enum):
    """
    Configured contracts
    """
    ERC20 = 1
    GMX_POSITION_ROUTER = 2
    GMX_ROUTER = 3
    GMX_READER = 4
    AAVE_POOL = 5
    AAVE_L2_ENCODER = 6
    AAVE_POOL_DATA_PROVIDER = 7
    COMPOUND_COMET = 8
    RADIANT_POOL = 9
    RADIANT_POOL_DATA_PROVIDER = 10
    SMA = 11
    SMA_FACTORY = 12
    SMA_MANAGER_ADMIN = 13
    SMA_ORACLE = 14
    SMA_ADDRESS_PROVIDER = 15
    SMA_MANAGEMENT_REGISTRY = 16
    SMA_MANAGEMENT_LOGIC = 17

class Events(Enum):
    """
    Events
    """
    SMACreated = 1

class RPCProviders(Enum):
    INFURA = 1
    ALCHEMY = 2
    QUICKNODE = 3
    CLOUDFLARE = 4
    CUSTOM = 5
    LOCAL = 6


class RPCEnv(Enum):
    MAIN = 1
    TEST = 2

class ChainIds(Enum):
    ARBITRUM = 42161
    OPTIMISM = 10
    ETH_MAIN = 1
    ETH_SEPOLIA = 11155111

class ConnectionTypes(Enum):
    HTTPS = 1
    WS = 2