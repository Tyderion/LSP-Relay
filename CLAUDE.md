# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

LSP-graphql is a Sublime Text plugin that provides GraphQL language support via the Language Server Protocol. It wraps the `graphql-language-service-server` from the GraphiQL project.

## Architecture

Two-component system:
- **Python plugin** (`plugin.py`): Sublime Text integration using `NpmClientHandler` from `lsp_utils`
- **Node.js language server** (`language-server/`): Thin wrapper around `graphql-language-service-server` that communicates via stdio

The plugin manages the Node.js server lifecycle automatically via `lsp_utils`.

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
- `language-server/start-server.js` - Server entry point, starts `graphql-language-service-server` with stdio method
- `language-server/package.json` - Node.js dependencies (`graphql`, `graphql-language-service-cli`)
- `LSP-graphql.sublime-settings` - Default plugin settings, selector targets `source.graphql`
- `dependencies.json` - Declares Sublime package dependencies (`lsp_utils`, `sublime_lib`)

## Code Style

- Python: Max line length 120 characters
- Do not use code regions
