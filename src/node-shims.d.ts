declare module 'node:fs/promises' { export function writeFile(path: string, data: Uint8Array | string): Promise<void>; }
declare module 'node:path' { export function join(...parts: string[]): string; }
declare module 'node:buffer' { export class Buffer extends Uint8Array { static from(data: ArrayBuffer | string): Buffer; toString(encoding?: string): string; } }
