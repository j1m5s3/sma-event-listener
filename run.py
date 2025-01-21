import asyncio

from pywin.mfc.object import Object

from app_logger.logger import Logger
from config_loader import (
    RPC_URL,
    CONTRACT_ADDRESSES,
    EVENT_ENV
)
from utils.constants.contract_events import EVENT_DEFINITIONS
from utils.constants.enums import Events, ConfiguredContracts
from interfaces.contract_event_listeners.base.base_listener_interface import BaseListenerInterface
from interfaces.contract_event_listeners.factory_listener_interface import SMAFactoryListenerInterface
from interfaces.contract_event_listeners.management_registry_listener_interface import SMAManagementRegistryListenerInterface
from interfaces.contract_event_listeners.management_logic_listener_interface import SMAManagementLogicListenerInterface

logger: Logger = Logger(section_name=f"{__name__}")


def get_listener_interface(event: Events) -> BaseListenerInterface:
    """
    Get the listener interface for the given event name

    :param event: Enum representing the event

    :return: Listener interface
    """
    if event in [Events.SMACreated]:
        listener_interface: SMAFactoryListenerInterface = SMAFactoryListenerInterface(
            ws_uri=RPC_URL,
            contract_address=CONTRACT_ADDRESSES[ConfiguredContracts.SMA_FACTORY],
            event_abi=EVENT_DEFINITIONS[event],
            event_name=event.name
        )
    elif event in [Events.ManagementStatusChanged]:
        listener_interface: SMAManagementRegistryListenerInterface = SMAManagementRegistryListenerInterface(
            ws_uri=RPC_URL,
            contract_address=CONTRACT_ADDRESSES[ConfiguredContracts.SMA_MANAGEMENT_REGISTRY],
            event_abi=EVENT_DEFINITIONS[event],
            event_name=event.name
        )
    elif event in [Events.InvestAction]:
        listener_interface: SMAManagementLogicListenerInterface = SMAManagementLogicListenerInterface(
            ws_uri=RPC_URL,
            contract_address=CONTRACT_ADDRESSES[ConfiguredContracts.SMA_MANAGEMENT_LOGIC],
            event_abi=EVENT_DEFINITIONS[event],
            event_name=event.name
        )
    else:
        raise NotImplementedError(f"Event {event.name} is not implemented")

    return listener_interface

async def create_tasks(events_list: list) -> None:
    tasks: list = []
    for event in events_list:
        task = asyncio.create_task(get_listener_interface(event).subscribe_to_event())
        tasks.append(task)

    await asyncio.gather(*tasks)


if __name__ == "__main__":
    logger.info(f"Running factory event listeners")
    if EVENT_ENV and isinstance(EVENT_ENV, Events):
        event: Events = EVENT_ENV
    else:
        event = Events.SMACreated

    asyncio.run(get_listener_interface(event).subscribe_to_event())
