var randomBytes = require("randombytes-shim");



for (var b = [], w = 0; w < 256; ++w)
            b[w] = (w + 256).toString(16).substr(1);

function E(t) {
            return function(t) {
                for (var e = [], n = 0; n < t.length; n++)
                    e.push(b[t[n]]);
                return e.join("")
            }(randomBytes(16)).substr(0, t)
        }

console.log("00-" + E() + "-" + E(16) + "-" + "01")


crypto=require("crypto-js")

var e = {
                        deviceType: 1
                    }

t='{"deviceType":1}/v1/entry/activity/ad/new/query?adSpaceCode=ZP-C-PC-POSITION-SIDEBAR&t=1678287961496'

t=crypto.SHA256(t).toString().toUpperCase()

Pt = crypto.enc.Utf8.parse("c558Gq0YQK2QUlMc")

It = function(t) {
                    kt = crypto.enc.Utf8.parse('/iEE205/5uqtjoofWPJ7sfwQ8=qBKCby'),
                    t = crypto.enc.Utf8.parse(t);
                    t = crypto.AES.encrypt(t, kt, {
                        iv: Pt,
                        mode: crypto.mode.CBC,
                        padding: crypto.pad.Pkcs7
                    });
                    return t.toString()
                }


console.log(It(JSON.stringify({
                        originHeader: JSON.stringify(e),
                        code: t
                    })))



// X-K-HEADER='1mz+3B7zUyPkqkueLDuG5XWLZpVti10X+P69SvVx24IeAX7PlY8gf6oDklIugZId'


qt = function() {
                    return JSON.stringify({
                        secret: '1mz+3B7zUyPkqkueLDuG5XWLZpVti10X+P69SvVx24IeAX7PlY8gf6oDklIugZId'
                    })
                }


console.log(qt())


const generatekey = num => {
  let library = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=';
  let key = '';
  for (let i = 0; i < num; i++) {
    let randomPoz = Math.floor(Math.random() * library.length);
    key += library.substring(randomPoz, randomPoz + 1);
  }
  return key;
};

console.log(generatekey(32))


//secretkeyvalue:https://gate.lagou.com/system/agreement

const rsa=require("node-rsa")

const rsaEncrypt = () => {
  const data = generatekey(32);
  // 注意只存一次aesKey

  // 公钥
  let publicKey =
    '-----BEGIN PUBLIC KEY-----' +
    'MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAnbJqzIX' +
    'k6qGotX5nD521Vk/24APi2qx6C+2allfix8iAfUGqx0MK3GufsQ' +
    'cAt/o7NO8W+qw4HPE+RBR6m7+3JVlKAF5LwYkiUJN1dh4sTj03X' +
    'Q0jsnd3BYVqL/gi8iC4YXJ3aU5VUsB6skROancZJAeq95p7ehXX' +
    'AJfCbLwcK+yFFeRKLvhrjZOMDvh1TsMB4exfg+h2kNUI94zu8MK' +
    '3UA7v1ANjfgopaE+cpvoulg446oKOkmigmc35lv8hh34upbMmeh' +
    'UqB51kqk9J7p8VMI3jTDBcMC21xq5XF7oM8gmqjNsYxrT9EVK7c' +
    'ezYPq7trqLX1fyWgtBtJZG7WMftKwIDAQAB' +
    '-----END PUBLIC KEY-----';
  let encrypt = new rsa(publicKey);

  const target = encrypt.encrypt(data,"base64");
  return target;
};



console.log(rsaEncrypt())





