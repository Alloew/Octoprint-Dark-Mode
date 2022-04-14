from __future__ import absolute_import

import octoprint.plugin

class DarkModePlugin(octoprint.plugin.types.OctoPrintPlugin, octoprint.plugin.core.SortablePlugin):
    def will_handle_ui(self, req):
        pass
    
    def on_ui_render(self, now, request, render_kwargs):
        pass

__plugin_pythoncompat__ = ">=2.7,<4"
__plugin_implementation__ = DarkModePlugin()