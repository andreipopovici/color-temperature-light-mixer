"""
Config flow schemas.

Schemas for the main configuration flow steps:
- User setup
- Reconfiguration

When this file grows too large (>300 lines), consider splitting into:
- user.py: User setup schemas
- reconfigure.py: Reconfiguration schemas
"""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any

import voluptuous as vol

from custom_components.color_temperature_light_mixer.const import (
    CONF_COLD_LIGHT,
    CONF_COLD_LIGHT_TEMPERATURE_KELVIN,
    CONF_CONSTANT_BRIGHTNESS_MODE,
    CONF_DEFAULT_COLD_LIGHT_TEMPERATURE,
    CONF_DEFAULT_WARM_LIGHT_TEMPERATURE,
    CONF_MAX_CONSTANT_BRIGHTNESS_LEVEL,
    CONF_WARM_LIGHT,
    CONF_WARM_LIGHT_TEMPERATURE_KELVIN,
    DEFAULT_CONSTANT_BRIGHTNESS_MODE,
    DEFAULT_MAX_CONSTANT_BRIGHTNESS_LEVEL,
)
from homeassistant.components.light.const import DOMAIN as LIGHT_DOMAIN
from homeassistant.const import CONF_NAME
from homeassistant.helpers import selector


def _suggested_value(defaults: Mapping[str, Any], key: str, fallback: Any) -> Any:
    """Return the current value to show in selector-backed form controls."""
    return defaults.get(key, fallback)


def get_user_schema(defaults: Mapping[str, Any] | None = None) -> vol.Schema:
    """
    Get schema for user step (initial setup).

    Args:
        defaults: Optional dictionary of default values to pre-populate the form.

    Returns:
        Voluptuous schema for user credentials input.

    """
    defaults = defaults or {}
    return vol.Schema(
        {
            vol.Required(
                CONF_NAME,
                default=defaults.get(CONF_NAME, vol.UNDEFINED),
            ): selector.TextSelector(
                selector.TextSelectorConfig(
                    type=selector.TextSelectorType.TEXT,
                ),
            ),
            vol.Required(
                CONF_WARM_LIGHT,
                default=defaults.get(CONF_WARM_LIGHT, vol.UNDEFINED),
            ): selector.EntitySelector(
                selector.EntitySelectorConfig(
                    filter=selector.EntityFilterSelectorConfig(domain=LIGHT_DOMAIN),
                )
            ),
            vol.Required(
                CONF_WARM_LIGHT_TEMPERATURE_KELVIN,
                default=defaults.get(CONF_WARM_LIGHT_TEMPERATURE_KELVIN, vol.UNDEFINED),
                description={
                    "suggested_value": _suggested_value(
                        defaults,
                        CONF_WARM_LIGHT_TEMPERATURE_KELVIN,
                        CONF_DEFAULT_WARM_LIGHT_TEMPERATURE,
                    ),
                },
            ): selector.ColorTempSelector(
                selector.ColorTempSelectorConfig(
                    unit=selector.ColorTempSelectorUnit.KELVIN,
                ),
            ),
            vol.Required(
                CONF_COLD_LIGHT,
                default=defaults.get(CONF_COLD_LIGHT, vol.UNDEFINED),
            ): selector.EntitySelector(
                selector.EntitySelectorConfig(
                    filter=selector.EntityFilterSelectorConfig(domain=LIGHT_DOMAIN),
                )
            ),
            vol.Required(
                CONF_COLD_LIGHT_TEMPERATURE_KELVIN,
                default=defaults.get(CONF_COLD_LIGHT_TEMPERATURE_KELVIN, vol.UNDEFINED),
                description={
                    "suggested_value": _suggested_value(
                        defaults,
                        CONF_COLD_LIGHT_TEMPERATURE_KELVIN,
                        CONF_DEFAULT_COLD_LIGHT_TEMPERATURE,
                    ),
                },
            ): selector.ColorTempSelector(
                selector.ColorTempSelectorConfig(
                    unit=selector.ColorTempSelectorUnit.KELVIN,
                ),
            ),
            vol.Required(
                CONF_CONSTANT_BRIGHTNESS_MODE,
                default=defaults.get(
                    CONF_CONSTANT_BRIGHTNESS_MODE,
                    DEFAULT_CONSTANT_BRIGHTNESS_MODE,
                ),
            ): selector.BooleanSelector(
                selector.BooleanSelectorConfig(),
            ),
            vol.Required(
                CONF_MAX_CONSTANT_BRIGHTNESS_LEVEL,
                default=defaults.get(
                    CONF_MAX_CONSTANT_BRIGHTNESS_LEVEL,
                    DEFAULT_MAX_CONSTANT_BRIGHTNESS_LEVEL,
                ),
                description={
                    "suggested_value": _suggested_value(
                        defaults,
                        CONF_MAX_CONSTANT_BRIGHTNESS_LEVEL,
                        DEFAULT_MAX_CONSTANT_BRIGHTNESS_LEVEL,
                    ),
                },
            ): selector.NumberSelector(
                selector.NumberSelectorConfig(
                    min=1,
                    max=100,
                    step=1,
                    mode=selector.NumberSelectorMode.SLIDER,
                    unit_of_measurement="%",
                ),
            ),
        },
    )


def get_reconfigure_schema(defaults: Mapping[str, Any]) -> vol.Schema:
    """
    Get schema for reconfigure step.

    Args:
        defaults: Optional dictionary of default values to pre-populate the form.

    Returns:
        Voluptuous schema for reconfiguration.

    """
    return vol.Schema(
        {
            vol.Required(
                CONF_WARM_LIGHT,
                default=defaults.get(CONF_WARM_LIGHT, vol.UNDEFINED),
            ): selector.EntitySelector(
                selector.EntitySelectorConfig(
                    filter=selector.EntityFilterSelectorConfig(domain=LIGHT_DOMAIN),
                )
            ),
            vol.Required(
                CONF_WARM_LIGHT_TEMPERATURE_KELVIN,
                default=defaults.get(CONF_WARM_LIGHT_TEMPERATURE_KELVIN, vol.UNDEFINED),
                description={
                    "suggested_value": _suggested_value(
                        defaults,
                        CONF_WARM_LIGHT_TEMPERATURE_KELVIN,
                        CONF_DEFAULT_WARM_LIGHT_TEMPERATURE,
                    ),
                },
            ): selector.ColorTempSelector(
                selector.ColorTempSelectorConfig(
                    unit=selector.ColorTempSelectorUnit.KELVIN,
                ),
            ),
            vol.Required(
                CONF_COLD_LIGHT,
                default=defaults.get(CONF_COLD_LIGHT, vol.UNDEFINED),
            ): selector.EntitySelector(
                selector.EntitySelectorConfig(
                    filter=selector.EntityFilterSelectorConfig(domain=LIGHT_DOMAIN),
                )
            ),
            vol.Required(
                CONF_COLD_LIGHT_TEMPERATURE_KELVIN,
                default=defaults.get(CONF_COLD_LIGHT_TEMPERATURE_KELVIN, vol.UNDEFINED),
                description={
                    "suggested_value": _suggested_value(
                        defaults,
                        CONF_COLD_LIGHT_TEMPERATURE_KELVIN,
                        CONF_DEFAULT_COLD_LIGHT_TEMPERATURE,
                    ),
                },
            ): selector.ColorTempSelector(
                selector.ColorTempSelectorConfig(
                    unit=selector.ColorTempSelectorUnit.KELVIN,
                ),
            ),
            vol.Required(
                CONF_CONSTANT_BRIGHTNESS_MODE,
                default=defaults.get(
                    CONF_CONSTANT_BRIGHTNESS_MODE,
                    DEFAULT_CONSTANT_BRIGHTNESS_MODE,
                ),
            ): selector.BooleanSelector(
                selector.BooleanSelectorConfig(),
            ),
            vol.Required(
                CONF_MAX_CONSTANT_BRIGHTNESS_LEVEL,
                default=defaults.get(
                    CONF_MAX_CONSTANT_BRIGHTNESS_LEVEL,
                    DEFAULT_MAX_CONSTANT_BRIGHTNESS_LEVEL,
                ),
                description={
                    "suggested_value": _suggested_value(
                        defaults,
                        CONF_MAX_CONSTANT_BRIGHTNESS_LEVEL,
                        DEFAULT_MAX_CONSTANT_BRIGHTNESS_LEVEL,
                    ),
                },
            ): selector.NumberSelector(
                selector.NumberSelectorConfig(
                    min=1,
                    max=100,
                    step=1,
                    mode=selector.NumberSelectorMode.SLIDER,
                    unit_of_measurement="%",
                ),
            ),
        }
    )


__all__ = [
    "get_reconfigure_schema",
    "get_user_schema",
]
