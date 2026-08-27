import fs from 'node:fs';
import path from 'node:path';

const root = path.resolve(new URL('..', import.meta.url).pathname);
const sources = [path.join(root, 'fortidlp', 'fortidlp.py'), ...fs.readdirSync(path.join(root, 'fortidlp'))
  .filter((file) => file.endsWith('.py') && file !== 'fortidlp.py')
  .sort().map((file) => path.join(root, 'fortidlp', file))];
const classes = {};
const sourceSymbols = {};

for (const filename of sources) {
  const source = fs.readFileSync(filename, 'utf8');
  const classMatches = [...source.matchAll(/^class\s+([A-Za-z_]\w*)[^:]*:/gm)];
  const fileSymbols = [];
  for (let index = 0; index < classMatches.length; index += 1) {
    const className = classMatches[index][1];
    if (['APIHandler', 'AuthenticationHandler'].includes(className)) continue;
    const start = classMatches[index].index + classMatches[index][0].length;
    const end = classMatches[index + 1]?.index ?? source.length;
    const classSource = source.slice(start, end);
    const methods = {};
    for (const match of classSource.matchAll(/^\s{1,8}def\s+([A-Za-z_]\w*)\s*\(([^)]*)\)/gm)) {
      const methodName = match[1];
      if (methodName === '__init__') continue;
      const params = match[2].split(',').map((part) => part.trim())
        .filter((part) => part && part !== 'self' && !part.startsWith('*'))
        .map((part) => part.split(':')[0].split('=')[0].trim()).filter(Boolean);
      const nextMethod = classSource.slice(match.index + match[0].length).match(/^\s{1,8}def\s+/m);
      const methodEnd = nextMethod ? start + match.index + match[0].length + nextMethod.index : end;
      const body = source.slice(start + match.index + match[0].length, methodEnd);
      const call = body.match(/(?:fortidlp_connection|self\.conn|self\.connection|self\.client)\.(get|send|post|insert|put|update|patch|delete|download|upload)\s*\(/);
      const downloadCall = body.match(/_download\s*\(/);
      if (!call && !downloadCall) continue;
      const directUrl = body.match(/(?:fortidlp_connection|self\.conn|self\.connection|self\.client)\.(?:get|send|post|insert|put|update|patch|delete|download|upload)\s*\(\s*f?["']([^"']+)["']/);
      const directBuiltUrl = body.match(/(?:fortidlp_connection|self\.conn|self\.connection|self\.client)\.(?:get|send|post|insert|put|update|patch|delete|download|upload)[\s\S]*?_build_url[\s\S]*?["']([^"']+)["']/);
      const assignedUrl = body.match(/url\s*=\s*f?["']([^"']+)["']/);
      const builtUrl = body.match(/_build_url[\s\S]*?["']([^"']+)["']/);
      const downloadedUrl = body.match(/_download[\s\S]*?["']([^"']+)["']/);
      const url = directUrl?.[1] ?? directBuiltUrl?.[1] ?? assignedUrl?.[1] ?? builtUrl?.[1] ?? downloadedUrl?.[1];
      if (!url) continue;
      const operation = call?.[1] ?? 'download';
      const explicitDownloadMethod = body.match(/method\s*=\s*["'](GET|POST|PUT|PATCH|DELETE)["']/)?.[1];
      const method = explicitDownloadMethod ?? (['send', 'post'].includes(operation) ? 'POST' : ['insert', 'put'].includes(operation) ? 'PUT' : operation === 'download' ? 'GET' : operation.toUpperCase());
      methods[methodName] = { params, method, url };
      fileSymbols.push(`${className}.${methodName}`);
    }
    if (Object.keys(methods).length) { classes[className] ??= {}; Object.assign(classes[className], methods); }
  }
  sourceSymbols[path.relative(root, filename)] = fileSymbols;
}

const output = path.join(root, 'src', 'generated-manifest.json');
fs.mkdirSync(path.dirname(output), { recursive: true });
fs.writeFileSync(output, `${JSON.stringify({ generatedFrom: sources.map((file) => path.relative(root, file)), classes, sourceSymbols }, null, 2)}\n`);
console.log(`Generated ${Object.keys(classes).length} classes and ${Object.values(classes).reduce((count, methods) => count + Object.keys(methods).length, 0)} methods.`);
