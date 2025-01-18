from models.events import SMACreated
from utils.constants.enums import ConfiguredContracts, Events
from interfaces.contracts.base.base_listener_interface import BaseListenerInterface

class SMAFactoryListenerInterface(BaseListenerInterface):
    """
    SMA Factory Listener Interface
    """

    event_abi: str  = "SMACreated(address,address,uint256,string)"
    event_name: str = Events.SMACreated.name

    def __init__(self, ws_uri: str, contract_address: str):
        super().__init__(
            ws_uri=ws_uri,
            event_definition=self.event_abi,
            contract_address=contract_address
        )

    def _unpack_event(self, event_dict: dict) -> dict:
        """
        Unpack event

        :param event_dict: Dictionary containing event data

        :return: Unpacked event
        """
        sma_created = SMACreated(raw_event=event_dict)
        return sma_created.model_dump()