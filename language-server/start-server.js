const { spawn } = require('child_process');

const relayBinary = require('relay-compiler');

if (relayBinary === null) {
    process.stderr.write(`Platform "${process.platform} (${process.arch})" not supported.\n`);
    process.exit(1);
}

const child = spawn(relayBinary, ['lsp'], {
    stdio: 'inherit'
});

child.on('error', (err) => {
    process.stderr.write(`Failed to start Relay LSP: ${err.message}\n`);
    process.exit(1);
});

child.on('exit', (code) => {
    process.exit(code || 0);
});
