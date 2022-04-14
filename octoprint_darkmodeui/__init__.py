from __future__ import absolute_import

import octoprint.plugin

class DarkModePlugin(octoprint.plugin.types.OctoPrintPlugin, octoprint.plugin.core.RestartNeedingPlugin):
    def get_assets(self):
        return dict(
            clientjs = ["clientjs/darkmode.js"]
        )

__plugin_pythoncompat__ = ">=2.7,<4"
__plugin_implementation__ = DarkModePlugin()