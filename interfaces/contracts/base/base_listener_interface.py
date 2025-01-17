import asyncio
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
            event: str,
            event_name: str,
            contract_address: str
    ):
        """
        Constructor

        :param ws_uri: String URI for websocket
        :param event: String event name with param types Ex. "EventName(address, uint256)"
        :param event_name: String event name
        :param contract_address:
        """
        self.event = Web3.keccak(text=event)
        self.contract_address = contract_address
        self.filter_params["address"] = contract_address
        self.filter_params["topics"] = [event]
        self.logger = Logger(section_name=f"{event_name}_listener")

        super().__init__(ws_uri)

    async def _subscribe_to_event(self) -> None:
        """
        Subscribe to event

        :return:
        """
        self.logger.info(f"Subscribing to event: {self.event}")

        async with AsyncWeb3(self) as w3:
            subscription_id = await w3.eth.subscribe(
                "logs",
                self.filter_params
            )
            self.logger.info(f"Subscription ID: {subscription_id}")

            async for event in w3.socket.process_subscriptions():
                decoded_event = decode(event["data"], [self.event])
                self.logger.info(f"Event: {decoded_event}")
        return

    def run(self) -> None:
        """
        Run listener

        :return:
        """
        self.logger.info("Running listener")
        asyncio.run(self._subscribe_to_event())
        return