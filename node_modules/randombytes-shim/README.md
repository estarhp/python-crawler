Tiny shim for `crypto.randomBytes` for nodejs & browsers.

```shell
	npm i randombytes-shim
```

Uses crypto / msCrypto implementations where available and falls back to using `Math.random()` in the worst case (e.g. IE11).

```javascript
	> var randomBytes = require("randombytes-shim");
	> console.log(randomBytes(3));
	Uint8Array [ 216, 210, 71 ]
```

Or use it directly in your HTML:

```html
	<script src="randombytes-shim.min.js"></script>
```
