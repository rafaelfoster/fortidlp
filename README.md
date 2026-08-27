# FortiDLP JavaScript/TypeScript client

This repository contains the original Python client and a Node.js client with
the same FortiDLP controller and method surface. The compiled `dist/` files
are included so another application can install the package directly from
GitHub.

```bash
npm install github:rafaelfoster/fortidlp#feat/typescript-client
```

```js
import { auth, Incidents } from 'fortidlp';

const login = await auth('FORTIDLP_HOST', 'ACCESS_TOKEN');
if (login.status) {
  const incidents = await new Incidents().search_incidents();
  console.log(incidents);
}
```

For development, run `npm install`, then `npm test`. `npm run build` rebuilds
the manifest from the Python sources and compiles TypeScript.
