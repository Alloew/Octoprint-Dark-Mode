from __future__ import absolute_import

import octoprint.plugin

class DarkModePlugin(octoprint.plugin.UiPlugin,
                          octoprint.plugin.TemplatePlugin):

    def will_handle_ui(self, request):
        pass

    def on_ui_render(self, now, request, render_kwargs):
        from flask import make_response
        return make_response("Hello World!")

__plugin_name__ = "DarkMode UI"
__plugin_pythoncompat__ = ">=2.7,<4"
__plugin_implementation__ = DarkModePlugin()