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
            ConfiguredContracts.SMA_FACTORY: "0xf8Ec37cbb381B23bF21EA0454CC91E7f66A382DE",
            ConfiguredContracts.SMA_MANAGER_ADMIN: "",
            ConfiguredContracts.SMA_ADDRESS_PROVIDER: "",
            ConfiguredContracts.SMA_ORACLE: "",
            ConfiguredContracts.SMA_MANAGEMENT_LOGIC: "",
            ConfiguredContracts.SMA_MANAGEMENT_REGISTRY: "0xeA28ad46c954A5d6B8C98EA31ef397EeD5317362",
        }
    }
}