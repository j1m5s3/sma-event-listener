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
            ConfiguredContracts.SMA_FACTORY: "0x31eca5Bba03d4b59Fc809B2231306020c5F295d5",
            ConfiguredContracts.SMA_MANAGER_ADMIN: "",
            ConfiguredContracts.SMA_ADDRESS_PROVIDER: "",
            ConfiguredContracts.SMA_ORACLE: "",
            ConfiguredContracts.SMA_MANAGEMENT_LOGIC: "0xED3Cdb25322cE3676C30Fe72Fb7604CbcB2B78eE",
            ConfiguredContracts.SMA_MANAGEMENT_REGISTRY: "0xb85ad49B6f7640a609f22D918fca0C04B7667b21",
        }
    }
}