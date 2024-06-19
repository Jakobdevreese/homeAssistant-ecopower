from homeassistant import config_entries
from homeassistant.core import callback
import voluptuous as vol
from .const import DOMAIN

@config_entries.HANDLERS.register(DOMAIN)
class P1MeterConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1

    async def async_step_user(self, user_input=None):
        if user_input is not None:
            return self.async_create_entry(title="P1 Meter", data=user_input)

        data_schema = vol.Schema({
            vol.Required("postcode"): str,
            vol.Required("tarief_1"): float,
            vol.Required("tarief_2"): float,
            vol.Required("productie_tarief_1"): float,
            vol.Required("productie_tarief_2"): float,
            vol.Required("maandpiek_sensor"): str,
        })

        return self.async_show_form(step_id="user", data_schema=data_schema)

    @staticmethod
    @callback
    def async_get_options_flow(config_entry):
        return P1MeterOptionsFlowHandler(config_entry)

class P1MeterOptionsFlowHandler(config_entries.OptionsFlow):
    def __init__(self, config_entry):
        self.config_entry = config_entry

    async def async_step_init(self, user_input=None):
        if user_input is not None:
            return self.async_create_entry(title="", data=user_input)

        data_schema = vol.Schema({
            vol.Required("postcode", default=self.config_entry.options.get("postcode", "")): str,
            vol.Required("tarief_1", default=self.config_entry.options.get("tarief_1", 0.0)): float,
            vol.Required("tarief_2", default=self.config_entry.options.get("tarief_2", 0.0)): float,
            vol.Required("productie_tarief_1", default=self.config_entry.options.get("productie_tarief_1", 0.0)): float,
            vol.Required("productie_tarief_2", default=self.config_entry.options.get("productie_tarief_2", 0.0)): float,
            vol.Required("maandpiek_sensor", default=self.config_entry.options.get("maandpiek_sensor", "")): str,
        })

        return self.async_show_form(step_id="init", data_schema=data_schema)