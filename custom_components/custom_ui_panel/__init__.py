"""Custom UI Panel integration."""

from __future__ import annotations

import logging

from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType

_LOGGER = logging.getLogger(__name__)


async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Set up the custom UI panel integration."""
    _LOGGER.debug("Setting up custom UI panel")

    hass.http.register_static_path("/custom_ui_panel", hass.config.path("custom_components/custom_ui_panel/www"), False)
    hass.components.frontend.async_register_built_in_panel(
        component_name="iframe",
        sidebar_title="Custom Panel",
        sidebar_icon="mdi:monitor-dashboard",
        frontend_url_path="custom-ui-panel",
        config={"url": "/custom_ui_panel/index.html"},
        require_admin=False,
    )

    return True
