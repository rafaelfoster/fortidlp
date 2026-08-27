import test from 'node:test';
import assert from 'node:assert/strict';
import manifest from '../src/generated-manifest.json' with { type: 'json' };
import * as client from '../dist/index.js';

const mockConnection = { get: async () => ({ status: true, data: null }), send: async () => ({ status: true, data: null }), post: async () => ({ status: true, data: null }), insert: async () => ({ status: true, data: null }), put: async () => ({ status: true, data: null }), update: async () => ({ status: true, data: null }), delete: async () => ({ status: true, data: null }) };
test('exports every Python controller', () => { for (const name of Object.keys(manifest.classes)) assert.equal(typeof client[name], 'function', name); });
test('exposes every Python controller method', () => { for (const [name, methods] of Object.entries(manifest.classes)) { const instance = new client[name](mockConnection); for (const method of Object.keys(methods)) assert.equal(typeof instance[method], 'function', `${name}.${method}`); } });
