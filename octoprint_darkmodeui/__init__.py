from __future__ import absolute_import
from cgitb import html

import octoprint.plugin

class DarkModePlugin(octoprint.plugin.types.OctoPrintPlugin, octoprint.plugin.core.SortablePlugin):
    def will_handle_ui(self, req):
        pass
    
    def on_ui_render(self, now, request, render_kwargs):
        from flask import make_response
        return make_response("<html><body>Dark Mode UI</body></html>", 200)

__plugin_pythoncompat__ = ">=2.7,<4"
__plugin_implementation__ = DarkModePlugin()