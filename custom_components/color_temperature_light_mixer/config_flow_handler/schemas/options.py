"""
Options flow schemas.

Schemas for the options flow that allows users to modify settings
after initial configuration.

When adding many options, consider grouping them:
- basic_options.py: Common settings (update interval, debug mode)
- advanced_options.py: Advanced settings
- device_options.py: Device-specific settings
"""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any

import voluptuous as vol

from custom_components.color_temperature_light_mixer.const import (
    CONF_CONSTANT_BRIGHTNESS_MODE,
    CONF_MAX_CONSTANT_BRIGHTNESS_LEVEL,
    DEFAULT_CONSTANT_BRIGHTNESS_MODE,
    DEFAULT_MAX_CONSTANT_BRIGHTNESS_LEVEL,
)
from homeassistant.helpers import selector


def _suggested_value(defaults: Mapping[str, Any], key: str, fallback: Any) -> Any:
    """Return the current value to show in selector-backed form controls."""
    return defaults.get(key, fallback)


def get_options_schema(defaults: Mapping[str, Any] | None = None) -> vol.Schema:
    """
    Get schema for options flow.

    Args:
        defaults: Optional dictionary of current option values.

    Returns:
        Voluptuous schema for options configuration.

    """
    defaults = defaults or {}
    return vol.Schema(
        {
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
    "get_options_schema",
]
