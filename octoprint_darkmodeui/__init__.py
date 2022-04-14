from __future__ import absolute_import

import octoprint.plugin

class DarkModePlugin(octoprint.plugin.AssetPlugin):
    def get_assets(self):
        # Include CSS files
        return dict(
            css=["css/darkmode.css"]
        )

__plugin_pythoncompat__ = ">=2.7,<4"

def __plugin_load__():
    global __plugin_implementation__
    __plugin_implementation__ = DarkModePlugin()