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
    def get_binary_arguments(cls) -> List[str]:
        settings = sublime.load_settings('LSP-relay.sublime-settings')
        args = []
        output_level = settings.get('lspOutputLevel', 'quiet-with-errors')
        if output_level:
            args.append('--output={}'.format(output_level))
        path_to_config = settings.get('pathToConfig', '')
        if path_to_config:
            args.append(path_to_config)
        return args
