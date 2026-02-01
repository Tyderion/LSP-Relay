# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

LSP-relay is a Sublime Text plugin that provides an LSP client for the Relay compiler's built-in language server. It enables diagnostics, autocomplete, go-to-definition, and other IDE features for Relay projects in JavaScript/TypeScript files.

## Architecture

Two-component system:
- **Python plugin** (`plugin.py`): Sublime Text integration using `NpmClientHandler` from `lsp_utils`
- **Node.js wrapper** (`language-server/`): Platform-detecting wrapper that spawns the native Relay compiler binary with the `lsp` argument

The Relay compiler ships platform-specific native binaries at `node_modules/relay-compiler/<platform>/relay`. The wrapper script detects the current platform and spawns the correct binary.

## Commands

**Install language server dependencies:**
```bash
cd language-server && npm install
```

**Python linting:**
```bash
flake8 plugin.py --max-line-length=120
pycodestyle plugin.py --max-line-length=120
```

## Key Files

- `plugin.py` - Plugin entry point, extends `NpmClientHandler`
- `language-server/start-server.js` - Wrapper that spawns the platform-specific relay binary with `lsp` argument
- `language-server/package.json` - Node.js dependencies (`relay-compiler`)
- `LSP-relay.sublime-settings` - Default plugin settings, selector targets JS/TS files
- `dependencies.json` - Declares Sublime package dependencies (`lsp_utils`, `sublime_lib`)

## Code Style

- Python: Max line length 120 characters
- Do not use code regions
