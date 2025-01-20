from pydantic import BaseModel, model_validator
from eth_abi.abi import decode

class BaseEvent(BaseModel):
    """
    Base event
    """
    raw_event: dict
    event_abi: str = None

class SMACreated(BaseEvent):
    """
    SMA created event
    """

    contract_address: str = None
    prospective_client: str = None
    ts_created: int = None
    event_abi: str = "SMACreated(address,address,uint256)"

    @model_validator(mode='after')
    def format_response(self):
        """
        Format response
        """
        self.contract_address = decode(["address"], self.raw_event['topics'][1])[0]
        self.prospective_client = decode(["address"], self.raw_event['topics'][2])[0]
        self.ts_created = decode(["uint256"], self.raw_event['topics'][3])[0]

        return self

class ManagementStatusChanged(BaseEvent):
    """
    Management status changed event
    """

    contract_address: str = None
    is_actively_managed: bool = None
    event_abi: str = "ManagementStatusChanged(address,bool)"

    @model_validator(mode='after')
    def format_response(self):
        """
        Format response
        """
        self.contract_address = decode(["address"], self.raw_event['topics'][1])[0]
        self.is_actively_managed = decode(["bool"], self.raw_event['topics'][2])[0]

        return self

class InvestAction(BaseEvent):
    """
    Invest action event
    """

    sma_address: str = None
    base_token_address: str = None
    amount: int = None
    from_protocol_address: str = None
    to_protocol_address: str = None
    event_abi: str = "InvestAction(address,address,uint256,address,address)"

    @model_validator(mode='after')
    def format_response(self):
        """
        Format response
        """
        self.sma_address = decode(["address"], self.raw_event['topics'][1])[0]
        self.base_token_address = decode(["address"], self.raw_event['topics'][2])[0]
        self.amount = decode(["uint256"], self.raw_event['topics'][3])[0]
        self.from_protocol_address, self.to_protocol_address = decode(["address", "address"], self.raw_event['data'])[0]

        return self

if __name__ == "__main__":
    # event_abi = SMACreated.model_dump()
    # print(event_abi)
    pass