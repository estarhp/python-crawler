const CryptoJS=require("crypto-js")

function b(a, b) {
        var c = CryptoJS.enc.Utf8.parse("BE45D593014E4A4EB4449737660876CE")
          , d = CryptoJS.enc.Utf8.parse("0102030405060708")
          , e = CryptoJS.enc.Utf8.parse(a)
          , f = CryptoJS.AES.encrypt(e, c, {
            iv: d,
            mode: CryptoJS.mode.CBC
        });
        return f.toString()
    }

console.log(b("李恩熙是哈麻批"))