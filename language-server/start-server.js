const { spawn } = require('child_process');
const path = require('path');
const os = require('os');

function getPlatformDir() {
    const platform = os.platform();
    const arch = os.arch();

    if (platform === 'darwin') {
        return arch === 'arm64' ? 'macos-arm64' : 'macos-x64';
    } else if (platform === 'linux') {
        return 'linux-x64';
    } else if (platform === 'win32') {
        return 'win32-x64';
    }
    throw new Error(`Unsupported platform: ${platform}-${arch}`);
}

const relayBinary = path.join(
    __dirname,
    'node_modules',
    'relay-compiler',
    getPlatformDir(),
    process.platform === 'win32' ? 'relay.exe' : 'relay'
);

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
