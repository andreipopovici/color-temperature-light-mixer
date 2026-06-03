"""Constants for color_temperature_light_mixer."""

from logging import Logger, getLogger

from homeassistant.components.light import ATTR_COLOR_TEMP_KELVIN
from homeassistant.const import CONF_ENTITY_ID

LOGGER: Logger = getLogger(__package__)

# Integration metadata
DOMAIN = "color_temperature_light_mixer"
ATTRIBUTION = "Data provided by http://jsonplaceholder.typicode.com/"
DEFAULT_NAME = "Color Temperature Light Mixer"

# Configuration entries
CONF_WARM_LIGHT = f"warm_light_{CONF_ENTITY_ID}"
CONF_WARM_LIGHT_TEMPERATURE_KELVIN = f"warm_light_{ATTR_COLOR_TEMP_KELVIN}"
CONF_COLD_LIGHT = f"cold_light_{CONF_ENTITY_ID}"
CONF_COLD_LIGHT_TEMPERATURE_KELVIN = f"cold_light_{ATTR_COLOR_TEMP_KELVIN}"

CONF_DEFAULT_WARM_LIGHT_TEMPERATURE = 3000
CONF_DEFAULT_COLD_LIGHT_TEMPERATURE = 6000
CONF_CONSTANT_BRIGHTNESS_MODE = "constant_brightness_mode"
CONF_MAX_CONSTANT_BRIGHTNESS_LEVEL = "max_constant_brightness_level"
DEFAULT_CONSTANT_BRIGHTNESS_MODE = False
DEFAULT_MAX_CONSTANT_BRIGHTNESS_LEVEL = 50

BRIGHTNESS_RANGE = (1, 255)
