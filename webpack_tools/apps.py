from django.apps import AppConfig
from django.core.management import call_command
from django.conf import settings


class WebpackToolsConfig(AppConfig):
    name = 'webpack_tools'
    verbose_name = "Django Webpack Tools"

    def ready(self):
        config = getattr(settings, "WEBPACK_TOOLS", {})
        if config.get("AUTOBUILD") is True:
            call_command('webpack build')