test = require("tape");
randomBytes = require("./randombytes-shim.min.js");

test("basic test", function(t) {
  t.plan(3);

  var b = randomBytes(3);
  t.true(b instanceof Uint8Array, "check type");
  t.equals(b.length, 3, "check length");
  t.true(b[0] <= 255, "check bounds");
});
