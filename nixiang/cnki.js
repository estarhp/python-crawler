const encrypt=require("crypto-js")


function s(t) {

     n = "95bae0e3871c9834"
            var e = {
                mode: encrypt.mode.ECB,
                padding: encrypt.pad.Pkcs7
            }
              , i = encrypt.enc.Utf8.parse(n)
              , s = encrypt.AES.encrypt(t, i, e)
              , r = s.toString().replace(/\//g, "_");
            return r = r.replace(/\+/g, "-"),
            r
        }


console.log(s("测试1"))
//'m6k8aW8fhEzCVdgQ4AS4Ww=='