from models.events import SMACreated
from utils.constants.enums import ConfiguredContracts, Events
from interfaces.contract_event_listeners.base.base_listener_interface import BaseListenerInterface

class SMAFactoryListenerInterface(BaseListenerInterface):
    """
    SMA Factory Listener Interface
    """

    def __init__(self, ws_uri: str, contract_address: str, event_abi: str, event_name: str):
        self.event_abi = event_abi
        self.event_name = event_name

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
        event_model = SMACreated(raw_event=event_dict)
        return event_model.model_dump()