import asyncio
from pydantic import BaseModel
from web3 import AsyncWeb3, WebSocketProvider, Web3
from eth_abi.abi import decode

from app_logger.logger import Logger


class BaseListenerInterface(WebSocketProvider):
    """
    Base listener interface

    https://web3py.readthedocs.io/en/stable/filters.html
    """

    event: bytes = None
    event_name: str = None
    contract_address: str = None
    filter_params: dict = {
        "address": None,
        "topics": None
    }

    logger: Logger = None

    def __init__(
            self,
            ws_uri: str,
            event_definition: str,
            contract_address: str
    ):
        """
        Constructor

        :param ws_uri: String URI for websocket
        :param event_definition: String event name with param types Ex. "EventName(address, uint256)"
        :param contract_address: Address of contract emitting event
        """
        self.event = Web3.keccak(text=event_definition)
        self.contract_address = contract_address
        self.filter_params["address"] = contract_address
        self.filter_params["topics"] = [self.event]
        self.logger = Logger(section_name=f"{self.event_name}_listener")

        super().__init__(ws_uri)

    def _unpack_event(self, event_dict: dict) -> dict:
        """
        Unpack event

        :param event_dict: Dictionary containing event data

        :return: Unpacked event
        """

    async def subscribe_to_event(self) -> None:
        """
        Subscribe to event

        :return:
        """
        self.logger.info(f"Subscribing to event: {self.event_name}")

        async with AsyncWeb3(self) as w3:
            subscription_id = await w3.eth.subscribe(
                "logs",
                self.filter_params
            )
            self.logger.info(f"Subscription ID: {subscription_id}")

            async for received_event in w3.socket.process_subscriptions():
                unpacked_event: dict = self._unpack_event(received_event['result'])
                self.logger.info(f"Event: {unpacked_event}")
        return


if __name__ == "__main__":
    ws_uri = "wss://mainnet.infura.io/ws/v3/your_project_id"
    event = "SMACreated(address,address,uint256,string)"
    event_name = "SMACreated"
    contract_address = "0x"
    listener = BaseListenerInterface(ws_uri, event, event_name, contract_address)
    asyncio.run(listener.subscribe_to_event())
