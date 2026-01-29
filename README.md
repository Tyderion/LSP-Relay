# LSP-relay

Relay language server support for Sublime Text's LSP plugin.

Uses the [Relay Compiler](https://relay.dev/docs/guides/compiler/) language server to provide diagnostics, autocomplete suggestions, and other features for Relay GraphQL fragments in JavaScript and TypeScript files.

## Installation

* Install [LSP](https://packagecontrol.io/packages/LSP) and `LSP-relay` from Package Control.
* Restart Sublime.

## Project configuration

The Relay language server requires a `relay.config.json` (or `relay.config.js`) in your project root with at minimum:

```json
{
  "src": "./src",
  "schema": "./schema.graphql",
  "language": "typescript"
}
```

Refer to the [Relay Compiler Configuration](https://relay.dev/docs/guides/compiler/) documentation for more details.

## Configuration

Open configuration file using command palette with `Preferences: LSP-relay Settings` command or opening it from the Sublime menu (`Preferences > Package Settings > LSP > Servers > LSP-relay`).
