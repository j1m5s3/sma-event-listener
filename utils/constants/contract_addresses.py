from utils.constants.enums import ConfiguredContracts, RPCEnv, ChainIds

CONTRACTS = {
    RPCEnv.MAIN: {
        ChainIds.ARBITRUM: {
            ConfiguredContracts.SMA_FACTORY: "",
            ConfiguredContracts.SMA_MANAGER_ADMIN: "",
            ConfiguredContracts.SMA_ADDRESS_PROVIDER: "",
            ConfiguredContracts.SMA_ORACLE: "",
            ConfiguredContracts.SMA_MANAGEMENT_LOGIC: "",
            ConfiguredContracts.SMA_MANAGEMENT_REGISTRY: "",
        }
    },
    RPCEnv.TEST: {
        ChainIds.ETH_SEPOLIA: {
            ConfiguredContracts.SMA_FACTORY: "0x20edE158C129416bfDB957DE907ce7f66295C797",
            ConfiguredContracts.SMA_MANAGER_ADMIN: "",
            ConfiguredContracts.SMA_ADDRESS_PROVIDER: "",
            ConfiguredContracts.SMA_ORACLE: "",
            ConfiguredContracts.SMA_MANAGEMENT_LOGIC: "0xB7ab994Cc254E7C98d5a3Ebe4e2CDe5A5bcdA3F9",
            ConfiguredContracts.SMA_MANAGEMENT_REGISTRY: "0x31550E2FB463F16c87730E84E7f2aE6F1Cd61A2b",
        }
    }
}