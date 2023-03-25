const CryptoJS=require("crypto-js")


 function Base64() {
            // private property
            _keyStr = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=";

            // public method for encoding
            this.encode = function (input) {
                var output = "";
                var chr1, chr2, chr3, enc1, enc2, enc3, enc4;
                var i = 0;
                input = _utf8_encode(input);
                while (i < input.length) {
                    chr1 = input.charCodeAt(i++);
                    chr2 = input.charCodeAt(i++);
                    chr3 = input.charCodeAt(i++);
                    enc1 = chr1 >> 2;
                    enc2 = ((chr1 & 3) << 4) | (chr2 >> 4);
                    enc3 = ((chr2 & 15) << 2) | (chr3 >> 6);
                    enc4 = chr3 & 63;
                    if (isNaN(chr2)) {
                        enc3 = enc4 = 64;
                    } else if (isNaN(chr3)) {
                        enc4 = 64;
                    }
                    output = output +
                        _keyStr.charAt(enc1) + _keyStr.charAt(enc2) +
                        _keyStr.charAt(enc3) + _keyStr.charAt(enc4);
                }
                return output;
            }

            // public method for decoding
            this.decode = function (input) {
                var output = "";
                var chr1, chr2, chr3;
                var enc1, enc2, enc3, enc4;
                var i = 0;
                input = input.replace(/[^A-Za-z0-9\+\/\=]/g, "");
                while (i < input.length) {
                    enc1 = _keyStr.indexOf(input.charAt(i++));
                    enc2 = _keyStr.indexOf(input.charAt(i++));
                    enc3 = _keyStr.indexOf(input.charAt(i++));
                    enc4 = _keyStr.indexOf(input.charAt(i++));
                    chr1 = (enc1 << 2) | (enc2 >> 4);
                    chr2 = ((enc2 & 15) << 4) | (enc3 >> 2);
                    chr3 = ((enc3 & 3) << 6) | enc4;
                    output = output + String.fromCharCode(chr1);
                    if (enc3 != 64) {
                        output = output + String.fromCharCode(chr2);
                    }
                    if (enc4 != 64) {
                        output = output + String.fromCharCode(chr3);
                    }
                }
                output = _utf8_decode(output);
                return output;
            }

            // private method for UTF-8 encoding
            _utf8_encode = function (string) {
                string = string.replace(/\r\n/g, "\n");
                var utftext = "";
                for (var n = 0; n < string.length; n++) {
                    var c = string.charCodeAt(n);
                    if (c < 128) {
                        utftext += String.fromCharCode(c);
                    } else if ((c > 127) && (c < 2048)) {
                        utftext += String.fromCharCode((c >> 6) | 192);
                        utftext += String.fromCharCode((c & 63) | 128);
                    } else {
                        utftext += String.fromCharCode((c >> 12) | 224);
                        utftext += String.fromCharCode(((c >> 6) & 63) | 128);
                        utftext += String.fromCharCode((c & 63) | 128);
                    }

                }
                return utftext;
            }

            // private method for UTF-8 decoding
            _utf8_decode = function (utftext) {
                var string = "";
                var i = 0;
                var c = c1 = c2 = 0;
                while (i < utftext.length) {
                    c = utftext.charCodeAt(i);
                    if (c < 128) {
                        string += String.fromCharCode(c);
                        i++;
                    } else if ((c > 191) && (c < 224)) {
                        c2 = utftext.charCodeAt(i + 1);
                        string += String.fromCharCode(((c & 31) << 6) | (c2 & 63));
                        i += 2;
                    } else {
                        c2 = utftext.charCodeAt(i + 1);
                        c3 = utftext.charCodeAt(i + 2);
                        string += String.fromCharCode(((c & 15) << 12) | ((c2 & 63) << 6) | (c3 & 63));
                        i += 3;
                    }
                }
                return string;
            }
        }




const  askOAwV97H7B = "aO3FNZwkSzMyoRHX";//AESkey，可自定义
const  asikLcpxpTx4 = "bEEgbt2HBUQ1GI60";//密钥偏移量IV，可自定义

const  ackdvGZN4qsY = "dLnlKg5FXA5L2flu";//AESkey，可自定义
const  aciU8RepD6bv = "fGhjOHudN5gUw4l3";//密钥偏移量IV，可自定义

const  dskBmLm2PW9J = "hpI122v0UGj1vwMA";//DESkey，可自定义
const  dsiR6ML3znuw = "x29suL1tVB6biMWW";//密钥偏移量IV，可自定义

const  dcksFAq2kxHJ = "odCmaZ7qqnkgqqtH";//DESkey，可自定义
const  dciT59vLqDrP = "p5PQAIekaqZskLZE";//密钥偏移量IV，可自定义

const aes_local_key = 'emhlbnFpcGFsbWtleQ==';
const aes_local_iv = 'emhlbnFpcGFsbWl2';

var BASE64 = {
    encrypt: function(text) {
        var b = new Base64();
        return b.encode(text);
    },
    decrypt: function(text) {
        var b = new Base64();
        return b.decode(text);
    }
};

var DES = {
 encrypt: function(text, key, iv){
    var secretkey = (CryptoJS.MD5(key).toString()).substr(0, 16);
    var secretiv = (CryptoJS.MD5(iv).toString()).substr(24, 8);
    secretkey = CryptoJS.enc.Utf8.parse(secretkey);
    secretiv = CryptoJS.enc.Utf8.parse(secretiv);
    var result = CryptoJS.DES.encrypt(text, secretkey, {
      iv: secretiv,
      mode: CryptoJS.mode.CBC,
      padding: CryptoJS.pad.Pkcs7
    });
    return result.toString();
 },
 decrypt: function(text, key, iv){
    var secretkey = (CryptoJS.MD5(key).toString()).substr(0, 16);
    var secretiv = (CryptoJS.MD5(iv).toString()).substr(24, 8);
    secretkey = CryptoJS.enc.Utf8.parse(secretkey);
    secretiv = CryptoJS.enc.Utf8.parse(secretiv);
    var result = CryptoJS.DES.decrypt(text, secretkey, {
      iv: secretiv,
      mode: CryptoJS.mode.CBC,
      padding: CryptoJS.pad.Pkcs7
    });
    return result.toString(CryptoJS.enc.Utf8);
  }
};

var AES = {
  encrypt: function(text, key, iv) {
    var secretkey = (CryptoJS.MD5(key).toString()).substr(16, 16);
    var secretiv = (CryptoJS.MD5(iv).toString()).substr(0, 16);
    // console.log('real key:', secretkey);
    // console.log('real iv:', secretiv);
    secretkey = CryptoJS.enc.Utf8.parse(secretkey);
    secretiv = CryptoJS.enc.Utf8.parse(secretiv);
    var result = CryptoJS.AES.encrypt(text, secretkey, {
      iv: secretiv,
      mode: CryptoJS.mode.CBC,
      padding: CryptoJS.pad.Pkcs7
    });
    return result.toString();
  },
  decrypt: function(text, key, iv) {
    var secretkey = (CryptoJS.MD5(key).toString()).substr(16, 16);
    var secretiv = (CryptoJS.MD5(iv).toString()).substr(0, 16);
    secretkey = CryptoJS.enc.Utf8.parse(secretkey);
    secretiv = CryptoJS.enc.Utf8.parse(secretiv);
    var result = CryptoJS.AES.decrypt(text, secretkey, {
      iv: secretiv,
      mode: CryptoJS.mode.CBC,
      padding: CryptoJS.pad.Pkcs7
    });
    return result.toString(CryptoJS.enc.Utf8);
  }
};

var localStorageUtil = {
  save: function(name, value) {
    var text = JSON.stringify(value);
    text = BASE64.encrypt(text);
    text = AES.encrypt(text, aes_local_key, aes_local_iv);
    try {
      localStorage.setItem(name, text);
    } catch (oException) {
      if (oException.name === 'QuotaExceededError') {
        // console.log('超出本地存储限额！');
        localStorage.clear();
        localStorage.setItem(name, text);
      }
    }
  },
  check: function(name) {
    return localStorage.getItem(name);
  },
  getValue: function(name) {
    var text = localStorage.getItem(name);
    var result = null;
    if (text) {
      text = AES.decrypt(text, aes_local_key, aes_local_iv);
      text = BASE64.decrypt(text);
      result = JSON.parse(text);
    }
    return result;
  },
  remove: function(name) {
    localStorage.removeItem(name);
  }
};

// console.log('base64', BASE64.encrypt('key'));

function ddInAzxepe7(pt4agtD) {
  pt4agtD = DES.decrypt(pt4agtD, dskBmLm2PW9J, dsiR6ML3znuw);
  return pt4agtD;
}

function dynhLIJy8o(pt4agtD) {
  pt4agtD = AES.decrypt(pt4agtD, askOAwV97H7B, asikLcpxpTx4);
  return pt4agtD;
}

function gSL5BQ9LwvjX0oLB(key, period) {
    if (typeof period === 'undefined') {
        period = 0;
    }
    var d = DES.encrypt(key);
    d = BASE64.encrypt(key);
    var data = localStorageUtil.getValue(key);
    if (data) { // 判断是否过期
        const time = data.time;
        const current = new Date().getTime();
        if (new Date().getHours() >= 0 && new Date().getHours() < 5 && period > 1) {
            period = 1;
        }
        if (current - (period * 60 * 60 * 1000) > time) { // 更新
           data = null;
        }
        // 防止1-5点用户不打开页面，跨天的情况
        if (new Date().getHours() >= 5 && new Date(time).getDate() !== new Date().getDate() && period === 24) {
           data = null;
        }
    }
    return data;
}

function ObjectSort(obj) {
    var newObject = {};
    Object.keys(obj).sort().map(function(key){
      newObject[key] = obj[key];
    });
    return newObject;
}
function d61LR0y6sy1Hrj5ylFrukuwi(data) {
    data = AES.decrypt(data, askOAwV97H7B, asikLcpxpTx4);
    data = DES.decrypt(data, dskBmLm2PW9J, dsiR6ML3znuw);
    data = BASE64.decrypt(data);
    return data;
}
var pWElSAP8joPbxbct = (function(){

function ObjectSort(obj){
    var newObject = {};
    Object.keys(obj).sort().map(function(key){
        newObject[key] = obj[key];
    });
    return newObject;
}
return function(method, obj){
    var appId = 'cd2753115f777a5cd6223ea60e478c8e';
    var clienttype = 'WEB';
    var timestamp = new Date().getTime();
    // console.log(method, obj,ObjectSort(obj),appId + method + timestamp + 'WEIXIN' + JSON.stringify(ObjectSort(obj)));
    var param = {
      appId: appId,
      method: method,
      timestamp: timestamp,
      clienttype: clienttype,
      object: obj,
      secret: CryptoJS.MD5(appId + method + timestamp + clienttype + JSON.stringify(ObjectSort(obj)))
    };
    param = BASE64.encrypt(JSON.stringify(param));
    param = DES.encrypt(param, dcksFAq2kxHJ, dciT59vLqDrP);
    return param;
}})()
console.log(pWElSAP8joPbxbct("GETDATA","青岛"))