import logging
from homeassistant.core import HomeAssistant
from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

async def async_setup(hass: HomeAssistant, config: dict):
    _LOGGER.info("Setting up Ecopower facturatie integration")
    return True

async def async_setup_entry(hass: HomeAssistant, entry):
    _LOGGER.info("Setting up Ecopower facturatie from config entry")
    return True