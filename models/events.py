from typing import Any
from pydantic import BaseModel, model_validator
from eth_abi.abi import decode

class SMACreated(BaseModel):
    """
    SMA created event
    """

    contract_address: str = None
    prospective_client: str = None
    ts_created: int = None
    message: str = None
    raw_event: dict
    event_abi: str = "SMACreated(address,address,uint256,string)"

    @model_validator(mode='after')
    def format_response(self):
        """
        Format response
        """
        raw_event_details: dict = self.raw_event

        self.contract_address = decode(["address"], raw_event_details['topics'][1])[0]
        self.prospective_client = decode(["address"], raw_event_details['topics'][2])[0]
        self.ts_created = decode(["uint256"], raw_event_details['topics'][3])[0]
        self.message = decode(["string"], raw_event_details['topics'][4])[0]

        return self

if __name__ == "__main__":
    # event_abi = SMACreated.model_dump()
    # print(event_abi)
    pass