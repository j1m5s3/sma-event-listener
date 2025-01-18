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
            ConfiguredContracts.SMA_FACTORY: "0xd909046Fd79d2adAC5CB2f3b059Ce159bcfFF739",
            ConfiguredContracts.SMA_MANAGER_ADMIN: "",
            ConfiguredContracts.SMA_ADDRESS_PROVIDER: "",
            ConfiguredContracts.SMA_ORACLE: "",
            ConfiguredContracts.SMA_MANAGEMENT_LOGIC: "",
            ConfiguredContracts.SMA_MANAGEMENT_REGISTRY: "",
        }
    }
}