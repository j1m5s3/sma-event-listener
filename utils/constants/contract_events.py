from utils.constants.enums import Events

EVENT_DEFINITIONS: dict = {
    Events.SMACreated: "SMACreated(address,address,uint256)",
    Events.ManagementStatusChanged: "ManagementStatusChanged(address,bool)",
}