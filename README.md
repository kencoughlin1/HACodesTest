# Home Assistant Custom UI Panel

This repository provides an example of a very simple custom integration for Home Assistant that adds a custom panel to the sidebar. The panel displays a static HTML page served by the integration.

## Installation

1. Copy the `custom_components/custom_ui_panel` folder into the `config/custom_components/` directory of your Home Assistant instance.
2. Restart Home Assistant.
3. After restart, a new sidebar entry called **Custom Panel** will appear. Selecting it will open the HTML page defined in `www/index.html`.

## Development

The integration registers the HTML page under `/custom_ui_panel/index.html` and uses Home Assistant's built-in `iframe` panel to display it.

You can modify `www/index.html` to add your own custom UI elements.
