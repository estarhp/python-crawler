function browserRandomValues(ar) {
  var crypto = window.crypto || window.msCrypto;
  if (crypto && crypto.getRandomValues) {
    return crypto.getRandomValues(ar);
  } else {
    return function (ar) {
      for (var i = 0; i < ar.length; i++) {
        ar[i] = Math.floor(256 * Math.random());
      }
    }
  }
}

function nodeRandomBytes(b) {
  return require("crypto").randomBytes(b);
}

module.exports = function getRandomBytes(b) {
  return (typeof(window) !== "undefined") ? browserRandomValues(new Uint8Array(b)) : Uint8Array.from(nodeRandomBytes(b));
}
