import fs from 'node:fs';
import path from 'node:path';
const root = path.resolve(new URL('..', import.meta.url).pathname);
const manifest = JSON.parse(fs.readFileSync(path.join(root, 'src/generated-manifest.json'), 'utf8'));
const built = fs.readFileSync(path.join(root, 'dist/index.js'), 'utf8');
const missing = Object.keys(manifest.classes).filter((name) => !built.includes(`export const ${name}`) && !built.includes(`export class ${name}`));
if (missing.length) { console.error('Missing controller exports:', missing); process.exitCode = 1; }
else console.log(`Surface check passed: ${Object.keys(manifest.classes).length} controllers, ${Object.values(manifest.classes).reduce((n, methods) => n + Object.keys(methods).length, 0)} methods.`);
