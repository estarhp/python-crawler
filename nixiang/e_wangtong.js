const cryto = require("crypto-js")
P = cryto.enc.Utf8.parse("20171109124536982017110912453698")
T = cryto.enc.Utf8.parse("2017110912453698")
Z = function(e) {
    var t, n;
    if (void 0 !== e)
        return e ? (t = e,
        n = cryto.enc.Utf8.parse(t),
        cryto.AES.encrypt(n, P, {
            iv: T,
            mode: cryto.mode.CBC,
            padding: cryto.pad.Pkcs7
        }).ciphertext.toString().toUpperCase()) : ""
}

console.log(Z("thyqwert"))