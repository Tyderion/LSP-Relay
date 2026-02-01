import os
import sublime
from lsp_utils import NpmClientHandler
from LSP.plugin.core.typing import List


def plugin_loaded() -> None:
    LspRelayPlugin.setup()


def plugin_unloaded() -> None:
    LspRelayPlugin.cleanup()


class LspRelayPlugin(NpmClientHandler):
    package_name = __package__
    server_directory = 'language-server'
    server_binary_path = os.path.join(server_directory, 'start-server.js')

    @classmethod
    def _get_setting(cls, key: str, default: str = '') -> str:
        # Check project-specific settings first
        window = sublime.active_window()
        if window:
            project_data = window.project_data() or {}
            project_settings = project_data.get('settings', {})
            lsp_settings = project_settings.get('LSP', {})
            relay_settings = lsp_settings.get('LSP-relay', {})
            if key in relay_settings:
                return relay_settings.get(key, default)
        # Fall back to global settings
        settings = sublime.load_settings('LSP-relay.sublime-settings')
        return settings.get(key, default)

    @classmethod
    def get_binary_arguments(cls) -> List[str]:
        args = []
        output_level = cls._get_setting('lspOutputLevel', 'quiet-with-errors')
        if output_level:
            args.append('--output={}'.format(output_level))
        path_to_config = cls._get_setting('pathToConfig', '')
        if path_to_config:
            args.append(path_to_config)
        return args
