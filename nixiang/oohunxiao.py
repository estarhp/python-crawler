# ==================================
# --*-- coding: utf-8 --*--
# @Time    : 2021-11-09
# @Author  : 微信公众号：K哥爬虫
# @FileName: replace_js.py
# @Software: PyCharm
# @describe: 混淆还原小脚本
# ==================================


# 待替换的值（太多了，仅列出少部分）
# 以实际列表为准，要和 fm_old.js 里的列表一致
item = [
    "gFxu",
    "fl",
    "bada",
    "static.fraudmetrix.cn",
    "or",
    "paramz",
    "rtcAvailable",
    "getEncodedHex",
    "fulfilled",
    "dec",
    "h",
    "_x64Add",
    "testBit",
    "deviceInfo",
    "wordwrap",
    "this is null or not defined",
    "key",
    "hczmaKxeRLPSY371ey",
    "zJHlaKEkRLhwYO71",
    "_reverseMap",
    "pvft",
    "/web/ub.png",
    "\n",
    "suffixes",
    "DERBoolean",
    "/fp/detect.json",
    "0c",
    "partnerCode",
    "languages",
    "https://static.tongdun.net/v3/3_8",
    "Times",
    "Android.*(wv|.0.0.0)",
    "am",
    "8.0",
    "r2",
    "zSHLIDELjIhriK7AeLUeJqfN",
    "Arial Unicode MS",
    "l",
    "posStart",
    "TEMPORARY",
    "zbHlaMEC",
    "malformed oid string: ",
    "hbRmawwXjzhFYyHFeQ",
    "setString",
    "VERTEX_SHADER",
    "frequencyBinCount",
    "task",
    "userAgentData",
    "F1",
    "parseUA",
    "phantomjs",
    "configurable",
    "_t41",
    "SET",
    "zsHpIDELjthLGP7aMaeobfxizx",
    "eruda",
    "webkitAudioContext",
    "factor",
    "browser",
    "F",
    "13",
    "doPrivate",
    "env",
    "firstChild",
    "canvas-fingerprint-defender-alert",
    "MSIE ([0-9]{1,}[.0-9]{0,})",
    "MOZILLA",
    "Requesting byte offset ",
    "onRejected",
    "h77umrlknir",
    "_xformMode",
    "04",
    "dingtalk",
    "TeletexString",
    "[object SafariRemoteNotification]",
    "indexedDB",
    "getExtension",
    "z1zmaWOLRm",
    "enumerable",
    "prototype",
    "zPzjIKEkRLPIGZ7FeaCEJgxI",
    "WEBKIT",
    ";",
    "unarmor",
    "device_name",
    "apply",
    "catch",
    "ASN.1 length too long to represent by 8x: n = ",
    "brand",
    "_deferreds",
    "S",
    "WINDOWSPHONE",
    "WINNDOWS",
    "= \f\n\r\t   ",
    " ",
    "normal",
    "1.2.840.113549.1.1.1",
    "zxHLIXE7juh9HF7AMaCcbKxizsOw",
    "staticHost",
    "android",
    "z6HCaKEgjthiY3pbePDpbFxmhPHlan",
    "&browser=",
    "device_version",
    "x-pnacl",
    "unpad",
    "DM",
    "GraphicString",
    "MAC",
    "Cambria",
    "msie",
    "gcda",
    " is not iterable(cannot read property Symbol(Symbol.iterator))",
    "UniversalString",
    "fromNumberAsync",
    "mmmmmmmmmmlli",
    "getRandomValues",
    "not",
    "xxid",
    "asn1",
    "_fmaa",
    "WEBGL_debug_renderer_info",
    "localDateToUTC",
    "re",
    "",
    " UTC",
    "explicit",
    "Offset: ",
    " elem)",
    "isEven",
    "…",
    "isFirefox",
    "g",
    "hPzDawEejzhLYG7lMaUeJEfgz1zw",
    "gecko",
    "<br/>(constructed)",
    "k",
    "iceServers",
    "appName",
    "Comic Sans MS",
    "tag",
    "NULL",
    "D",
    "canvas",
    "<br/>Value:<br/><b>",
    "partnerSendSwitch",
    "__nightmare",
    "tokens",
    "sans-serif",
    "RegExp out of sync",
    "_selenium",
    "\"function() {\\n      if (script.dataset.active === 'true') {\\n        try {\\n          this.manipulate();\\n        }\\n        catch(e) {\\n          console.warn('manipulation failed', e);\\n        }\\n      }\\n      return toDataURL.apply(this, arguments);\\n    }\"",
    "win",
    "ghijklmnopqrstuv",
    "_ks",
    "fmTest",
    "zPHlaMECjzhriy71eTUpbXxIzS",
    "header",
    "Firefox",
    "lShiftTo",
    "default_key_size",
    "(.{1,",
    "clearBit",
    "requestPermission",
    "height",
    "Malformed UTF-8 data",
    "setByBinaryString",
    "(",
    "PointerEvent",
    "CipherParams",
    "parseStringUTF",
    "30",
    "caller",
    "os",
    "insertBefore",
    "getLowestSetBit",
    "BqAH",
    "allSettled",
    "offsetUniform",
    "innerHeight",
    "multiply",
    "getHighEntropyValues",
    "pjlF",
    "parseInteger",
    "mozRTCPeerConnection",
    "FfhJ",
    ".",
    "16",
    "ulen",
    "Ijcz",
    "d",
    "6",
    "disconnect",
    "removeEventListener",
    "zSHLIDELjIhrHq7FMZUEbXgtzVzma1Eg",
    "iUrl",
    "getItem",
    "base64s",
    "mimeTypes",
    "pad",
    "zJHpanEFRuhLYx7A",
    "usageDetails",
    "fontFamily",
    "value hex must be even length: n=",
    "u",
    "connection",
    "opr",
    "r",
    "index",
    "isBlink",
    "Lucida Handwriting",
    "ECvA",
    "I",
    "CHROME",
    "3",
    "zVzDIoO7jOhDYy",
    "cookieStore",
    "cookie",
    "hexDump",
    "LINUX",
    "WebOS",
    "device_type",
    "multiplyUpperTo",
    "appendASN1Object",
    "x-nacl",
    "appVersion,language,languages,mimeTypes,oscpu,platform,plugins,userAgent",
    "_data",
    "head",
    "Webkit",
    "4",
    "isProbablePrime",
    "INTEGER",
    "date",
    "fillText",
    "Mozilla",
    "onmouseover",
    "18",
    "MACAddress",
    "ARRAY_BUFFER",
    "_nDataBytes",
    "w3",
    "tdfp",
    "knee",
    "w",
    "zPHda1EGjlPIiY7Ae4UDbpfj",
    "q3",
    "Wingdings 2",
    "setLocalDescription",
    "salt",
    "linkProgram",
    "aomygod",
    "DERObjectIdentifier",
    "h0HLaXEFjCQHYK7blz",
    "VConsole",
    "screenX",
    "EXTERNAL",
    "charAt",
    "msg",
    "functiontoString(){[nativecode]}",
    "initialized",
    "storage",
    " @",
    "oid",
    "parseTime",
    "this.hV is null or undefined.",
    "destination",
    "substring",
    "q",
    "Verdana",
    "host",
    "Lucida Sans Typewriter",
    "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz",
    "ActiveXObject",
    "EvpKDF",
    "isChrome",
    "<br/>",
    "version",
    "createDataChannel",
    "Content size is not correct for container starting at offset ",
    "dmq1",
    "VideotexString",
    "DERGeneralizedTime",
    "toString",
    "itsgonnafail",
    "DERBitString",
    "_cipher",
    "zPHpanwXjOPFHq7FMZUEbX",
    "hPHjIXEGjuhiiG7AeGCf",
    "a",
    "CBC",
    "functionget(){[nativecode]}",
    "zJHpanEFRuhLYx7AMN",
    "iphone",
    "symbol",
    "op",
    "flipBit",
    "defineProperty",
    "browserType2",
    "uniformOffset",
    "h1zjawwrtChLYp79MzUibExI",
    "zSHLaXwGjtQIYO7aeH",
    "document",
    "Bitstream Vera Sans Mono",
    "_keyPriorReset",
    "&productType=2",
    "cssText",
    "appendChild",
    "hSHQaIEGREhHYp7A",
    "level",
    "modPow",
    "TOUCHPAD",
    "sine",
    "Object",
    "pos",
    "FRAGMENT_SHADER",
    "fillRect",
    "lib",
    "estimate",
    "attachEvent",
    "BMPString",
    "https://bugly.tongdun.net/bugly/errorCollect/v1.png",
    "; expires=Thu, 01-Jan-70 00:00:01 GMT;",
    "EMBEDDED_PDV",
    "DERSequence",
    "U",
    "4enw49pim03",
    "getValueHex",
    "useProgram",
    "boolean",
    "negate",
    "BADA",
    "item",
    "IA5String",
    "Uburl",
    "_fmOpt.partner is blank, please set the value of _fmOpt.partner and try again!",
    "hSHlJKwhRVhwYp79NNCfJqxNzsHK",
    "dMultiply",
    "divRemTo",
    "wk",
    "Android",
    "localStorage",
    "ios",
    "integerToByteHex",
    "TouchEvent",
    "9",
    "webgl-fingerprint-defender",
    "_minBufferSize",
    "X",
    "useSid",
    "未定义",
    "battery",
    "detect",
    "_ENC_XFORM_MODE",
    "cookieHandler",
    "_TDctimestamp",
    "mph",
    "behaviorUrl",
    "Utf8",
    "_mode",
    "8",
    "application/hwepass2001.installepass2001",
    "unused bits shall be from 0 to 7: u = ",
    "BLACKBERRY",
    ",length:",
    "createProgram",
    "en-US,en",
    "getHexStringValue",
    "screenTop",
    "zVzcaQELjCQqY37bMQUo",
    "R",
    "WbemScripting.SWbemLocator",
    "availHeight",
    "31",
    "RegExp",
    "Base64 encoding incomplete: at least 2 bits missing",
    "removeHandler",
    "tdIframe",
    "9LzjkIEhqu",
    "propertyIsEnumerable",
    "platform",
    "DERTeletexString",
    ",sub:",
    "fromCharCode",
    "o8gm8qu97as",
    "hTLV",
    "mp",
    "amap",
    "Consolas",
    "Lucida Fax",
    "equals",
    "divideAndRemainder",
    "exp",
    "BB26C2E91BA08EFB",
    "Times New Roman",
    "Length: ",
    "getPublicBaseKey",
    "initStorage",
    "rtcFinished",
    "UNMASKED_VENDOR_WEBGL",
    "hPHjIXEGjuhiiY7aePUA",
    "parseKey",
    "writable",
    "_invKeySchedule",
    "callPhantom",
    "Promise.all accepts an array",
    "2.3.1",
    "s38huiupo1g",
    "pow",
    "Tahoma",
    "success",
    "Object.keys called on non-object",
    "value",
    "z1HCIwEctLhrGF7FeNUEJd",
    "coeff",
    "function",
    "GECKO",
    "Courier New",
    "zsHpINELRBhriG7AeqUDJgxs",
    "Microsoft Internet Explorer",
    "360SE",
    "Trebuchet MS",
    "window",
    "vertexPosArray",
    "warn",
    " (constructed)",
    "zBmz",
    "webgl-fingerprint-defender-alert",
    "(Windows NT 10.0; Win64; x64",
    "ANDROID",
    "_DEC_XFORM_MODE",
    "newValue",
    "abcdefghjiklmnopqrstuvwxyz",
    "_state",
    "characterSet",
    "(iPhone|iPod|iPad)(?!.*Safari/)",
    "ipad",
    "encode",
    "addres",
    "_k41",
    "sort",
    "createElement",
    "+",
    "DERUTF8String",
    "getElementById",
    "WordArray",
    " \f\n\r\t   ",
    "enabled",
    "opera",
    "outerHeight",
    "OID",
    "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789",
    "#069",
    "Chromium",
    "productSub",
    "ubid",
    "gDDI",
    "05",
    "content",
    "Impact",
    "zVzLaNELjKQFGPple4U5bE",
    "monospace",
    "Array.prototype.indexOf() - can't convert `",
    "contentWindow",
    "alphabetic",
    "channelCountMode",
    "_value",
    "EOC",
    "Palatino Linotype",
    "tIndex",
    "enc",
    "` to object",
    "kjxz",
    "&sdkVersion=",
    "toHexString",
    "webkitBattery",
    "&lt;",
    "b",
    "vertexPosAttrib",
    "position:absolute !important; z-index:-9999 !important; visibility:hidden !important;border:0 !important",
    "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCuR3+MuPOVYuAKOS6O+J/ds+JAesgyFforFupDiDBBMTItdXyMrG6gUPFxj/pT/9uQSq8Zxl7BrdiKdi0G2ppEn4Nym+VRLTv2+lNa3kvlrj25Lop7wDZkVRecK5oDvdaQHrm4KKiF7jZNbHEreWGsINLpGvzBMRNztRtOJ6+XEQIDAQAB",
    "vDHC",
    "extend failed, please check that ",
    "platformVersion",
    "obj",
    "Private_",
    "M",
    "url",
    "OCTET_STRING",
    "1",
    "ONE",
    "posEnd",
    "DB",
    "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/",
    "outro",
    "zRzLINEGRVrRYy7FeyUoJg",
    "  ",
    "type",
    "createAnalyser",
    "Lucida Calligraphy",
    "bitwiseTo",
    "subtract",
    "|",
    "partner",
    "zSHLaXwGjtQIY37Wez",
    "hasPublicKeyProperty",
    "usage",
    "posContent",
    "and",
    "fpNetHost",
    "every",
    "result",
    "detectEthernet",
    "netscape",
    "zoom",
    "Promises must be constructed via new",
    "partnerFpUrl",
    "&sdkName=cn.tongdun.web",
    "enableVertexAttribArray",
    "_IEEnumFix",
    "connect",
    "availWidth",
    "DERTaggedObject",
    "IPAD",
    "zNHpaEELjIhwYOpAMNecJqfs",
    "mulTo",
    "IOS",
    "max",
    "getString",
    "fakeHover",
    "__IE_DEVTOOLBAR_CONSOLE_COMMAND_LINE",
    "onFulfilled",
    "wsHost",
    "DOLFIN",
    "~/",
    "&occurTime=",
    "mediaDevices",
    "xiamenair",
    "dlen",
    "zding_",
    "absolute",
    "360EE",
    "_key",
    "x-google-chrome-pdf",
    "-webkit-hyphens",
    "adblock2345",
    "tDkG",
    "hL",
    "btmz",
    "m",
    "Wingdings",
    "zIHlanwhRIr9Y3pYMQ",
    "sandbox",
    "object",
    "hex",
    "page:",
    "andNot",
    "gk",
    "drShiftTo",
    "bufferData",
    "HTMLScriptElement",
    "presto",
    "charCodeAt",
    "font",
    "72px",
    "htHdaQwhjBhHGZ7WNGUEJqfgz6Hlan",
    "Z",
    "L",
    "nextBytes",
    "htHdaQwhjBhHGZ7W",
    "keys",
    "hPHjIXEGjuhiHP7aMr",
    "toHexDOM_sub",
    "modInt",
    "not a function",
    "; domain=",
    "timeout",
    "MicroMessenger",
    "DERNull",
    "&osVersion=",
    "attribute vec2 attrVertex;varying vec2 varyinTexCoordinate;uniform vec2 uniformOffset;void main(){varyinTexCoordinate=attrVertex+uniformOffset;gl_Position=vec4(attrVertex,0,1);}",
    "webgl",
    "_x64Xor",
    "__wxjs_environment",
    "y",
    "getImageData",
    "function(){[nativecode]}",
    "setPublicKey",
    "innerHTML",
    "gnpp",
    "Trident",
    "getPrivateBaseKey",
    "numberOfInputs",
    "setKey",
    "remainder",
    "_",
    "Century Gothic",
    "https://fptest.fraudmetrix.cn/partnerProfile.json",
    "ongestureend",
    "0",
    "onsuccess",
    "tzso",
    "-&-",
    "attachShader",
    "SEQUENCE",
    "then",
    "reject",
    "zcHpINwhjuPSG3",
    "constructor",
    "_unhandledRejectionFn",
    "filename",
    "userData",
    "CbGz",
    "flush",
    "referrer",
    "chromeos",
    "Andale Mono",
    "href",
    "$1\r\n",
    "rShiftTo",
    "zPHpanwXjOPFHP7aoQUiJgxmi10wkExeRLPSY371ey",
    "hSHQaIEGRIPIYS7WMr",
    "bindBuffer",
    "#f60",
    "_prevBlock",
    "_immediateFn",
    "Y",
    "createEvent",
    "abs",
    "jyru",
    "rhino",
    "iterator",
    "__defineGetter__",
    "Segoe UI Semibold",
    "pageInfo",
    "oncomplete",
    "O",
    "iPhone",
    "um",
    "shaderSource",
    "blackBox",
    "OfflineAudioContext",
    "compatible",
    "Cipher",
    "floor",
    "htHdIwEFjzhiGMqYMQCpbKx9z0",
    "application/360softmgrplugin",
    "mu",
    "BufferedBlockAlgorithm",
    "initCookie",
    "VisibleString",
    "write",
    "zIzLanEeRLhwYO71eHUEb6xHhSHv",
    "Arial Black",
    "&h=",
    "zNzjkIEkRUQIYOpAeNUoK7xiz6HCINwe",
    "expected",
    "body",
    "Mac OS",
    "webkitRequestFileSystem",
    "REAL",
    "postMessage",
    "a0",
    "G",
    "Exception while decoding undefined length content: ",
    "@",
    "charset",
    ":",
    "release",
    "join",
    "/v3/fm.js",
    "Pkcs7",
    "hexDigits",
    "reCheckCookie",
    "cdu",
    "z1HCIwEcjuPSYSpbezefbFfZz6HjawweSIPIGZ7FeqUD",
    "Century Schoolbook",
    "userAgent",
    "saveData",
    "ldDF",
    "ExecQuery",
    "debug",
    "string",
    "location",
    "Hmqb",
    "zRzjaKw8Ru",
    "tao",
    "MSIE (\\d+\\.\\d+);",
    "_TDopnum",
    "fromNumber",
    "generateAsync",
    "abcdefghigklmn",
    "h1zjawwrtOhqYy71MQ",
    "push",
    "unload",
    "F2",
    ",v=",
    "_utf8_encode",
    "enumerateDevices",
    "s",
    "z6HCanEGRVQqY37bMQUo",
    "set",
    "Garamond",
    "FV",
    "V",
    "FormData",
    "FIqG",
    "reuy",
    "windows",
    "Hxuw",
    "browserVersion2",
    "application/",
    "&errorMsg=",
    "_t16",
    "plugins",
    "Base",
    "DERAbstractTime",
    "0500",
    "__BROWSERTOOLS_DOMEXPLORER_ADDED",
    "DERObjectIdentifier oidName undefined: ",
    "multiplyTo",
    "ie",
    "font-fingerprint-defender",
    "revert",
    "zxHLIXE7juh9iFplePUaldxaz6HLanwh",
    "screenY",
    "00000000",
    "GeneralizedTime",
    "z0HLINOFRmPr",
    "pushNotification",
    "phantomas",
    "BlockCipherMode",
    "oyo",
    "text-align-last",
    "outerWidth",
    "_xid",
    "consoleCheck",
    "Edg/",
    "div",
    "/FreshCookieRequest/fresh.json",
    "navigator",
    "crios",
    "changeBit",
    "newFalseArray",
    "https",
    "DEROctetString",
    "_x64LeftShift",
    "pTimeout",
    "undefined",
    "H",
    "zVzLaNELjKrFYO71MQUEJpfj",
    "x",
    "cacheKeyBlackbox",
    "copyTo",
    "createDynamicsCompressor",
    "MS Reference Sans Serif",
    "RIMTABLET",
    "secure",
    "tokenId",
    "q652mrpq0k",
    "detectSwitch",
    "BlockCipher",
    "sqrTo",
    "HmacMD5",
    "isModified",
    "ch",
    "0.0.0.0",
    "?",
    "dlShiftTo",
    "sin",
    "lineHeight",
    "zbHpIXEhRthLGZ7AoNUeb6xgh1zwIXEGjlhFG3",
    "IE",
    "zbHLaQEhjChrGMpYNaUEbjfgzRHC",
    "setByInteger",
    "air",
    "random",
    "CTR",
    "CHROMEOS",
    "toPrettyString",
    "Decryptor",
    "z",
    "hSHlIwEejUQFGyp2MrUeJqfj",
    " is not a function",
    "lzbH",
    "experimental-webgl",
    "hT",
    " (encapsulates)",
    "1234567890",
    "[object Function]",
    "decrypt",
    "c",
    "zPHvaQwrRIhrGP",
    "RTCPeerConnection",
    "toLocaleString",
    "f",
    "shiftRight",
    "ua",
    "hasContent",
    "ObjectDescriptor",
    "gesture",
    "firefox",
    "})",
    "2d",
    "partnerDetectUrl",
    "function()",
    "cookieEnabled",
    "ASN1Util",
    "Imnb",
    "ceil",
    "20030107",
    "major",
    "rimtablet",
    "&os=",
    "IPOD",
    "o",
    "left",
    "match",
    "mobile",
    ")",
    "_nRounds",
    "from",
    "utc",
    "numberOfOutputs",
    "extend",
    "/",
    "i.html",
    "17",
    "$super",
    "split",
    "audiocontext-fingerprint-defender",
    "ct",
    "textBaseline",
    "channelInterpretation",
    "TAOBAO",
    "top",
    "mozBattery",
    "p",
    "SyntaxError",
    "getAttribLocation",
    "modPowInt",
    "parseStringISO",
    "micromessage",
    "\\",
    "can't find _fmOpt",
    "@script",
    "Lucida Bright",
    "addEventListener",
    "intValue",
    "application/mozilla-npqihooquicklogin",
    "init",
    "ub",
    "DERPrintableString",
    "allow-scripts",
    "console",
    "Shockwave Flash",
    "wm",
    "indexOf",
    "convert",
    "RequestFileSystem",
    "rejected",
    "; expires=",
    "$1",
    "zVzDIoOcjzhiYOplNGUEJqfgz6Hlan",
    "width",
    "finally",
    "msMaxTouchPoints",
    "setValueHex",
    "cacheKeyBlackboxTimestamp",
    "uniform2f",
    "screenLeft",
    "exec",
    "chunkSize",
    "setByDateValue",
    "next",
    "addons",
    "Edge",
    "race",
    "start",
    "showModalDialog",
    "LUCIDA GRANDE",
    "Segoe UI",
    "DERAbstractString",
    "map",
    "?platform=3",
    "webkitOfflineAudioContext",
    "_TDfactor",
    "serif",
    ",",
    "010001",
    "zqoF",
    "ig",
    "WebView",
    "_x64Multiply",
    "Lucida Sans",
    "_handled",
    "Constructor",
    "intro",
    "https://xx.com",
    "desktop",
    "https://fp.fraudmetrix.cn",
    "Palatino",
    "getLengthHexFromValue",
    "onerror",
    "isFunction",
    "Arial Hebrew",
    "setHexValueIncludingUnusedBits",
    "=; domain=",
    "/web3_8/profile.json",
    "getContext",
    "<br/>(encapsulates)",
    "clone",
    "Times New Roman PS",
    "Monotype Corsiva",
    "2345Explorer",
    "getSeconds",
    "n",
    "zPHda1EGjlPIHx7FeQCfbp",
    "min",
    "zPHpanwXjOPFiy7WMrCfJKgjzRRmaQwhjOQrHZHS",
    "[",
    "zVzDIoxXjuPSGM7FePU5",
    "drawArrays",
    "zNHpanwGjBhLYMpbMzCpbFft",
    "reduce",
    "unable to locate global object",
    "ABCDEFGHJIKLMNOPQRSTUVWXYZ",
    "E",
    "hexNode",
    "eEBd",
    "A promise cannot be resolved with itself.",
    "IbdE",
    "macintosh",
    "resolve",
    "Universal_",
    "rv:11.0",
    "Latin1",
    "06",
    "jsonUrl",
    "base64_map",
    "] expected ",
    "Arial",
    "j",
    "signum",
    "device-version",
    "getError",
    "Century",
    "SILK",
    "<br/>(warning!)",
    "hJFw",
    "ConnectServer",
    "getPEMStringFromHex",
    "-----\r\n",
    "HTMLElement",
    "CrOS",
    "jsDownloadedTime",
    " (undefined)",
    "_utf8_decode",
    "0123456789",
    "hyhbgqbaxi6",
    "gFlu",
    "parsePropertiesFrom",
    "http://fp.fraudmetrix.cn",
    "parseOID",
    "functionlog(){[nativecode]}",
    "position",
    "[object Object]",
    "offsetHeight",
    "Segoe UI Symbol",
    "superclass",
    "kernelVersion2",
    "en-US",
    "mt2",
    "DERAbstractStructured",
    "Microsoft Sans Serif",
    "Select * from Win32_NetworkAdapterConfiguration Where IPEnabled =True",
    "zPHpanwXjOPF",
    "parseOctetString",
    "zSHLaXwGjthqYyplNaUEbjfgzRHC",
    "subTo",
    "null",
    "values",
    "invDigit",
    "parse",
    "UTC",
    "createTextNode",
    "onmessage",
    "crypto",
    "caja",
    "fromInt",
    "00",
    "(){[nativecode]}",
    "UTF8String",
    "documentMode",
    "readPixels",
    " bit)",
    "algo",
    "all dependencies are included.",
    "SAFARI",
    "J",
    "getOwnPropertyDescriptor",
    "referer",
    "timestamp",
    "toDOM",
    "noIframe",
    "via",
    "CSS",
    "writeln",
    "'WebSocket' is undefined",
    "common2345",
    "isWebkit",
    "Helvetica Neue",
    "getDate",
    "precision mediump float;varying vec2 varyinTexCoordinate;void main() {gl_FragColor=vec4(varyinTexCoordinate,0,1);}",
    "dp",
    "message",
    "fmData",
    "Comic Sans",
    "MYRIAD PRO",
    "compute",
    "T",
    "_x64Rotl",
    "text",
    "Length over 24 bits not supported at position ",
    "length",
    "add",
    "zczwaMwFRIhrGZqRezCpJdxNzRHChX",
    "concat",
    "Math",
    "multiplyLowerTo",
    "79F05CA5AF1CAE77",
    "maxTouchPoints",
    "zumk",
    "fp.fraudmetrix.cn:9090",
    "threshold",
    "zczwaMwFRIhrGZHSeTU5bEfIzVHKaw",
    "bigint",
    "C",
    "getFloatFrequencyData",
    "token",
    "DeviceMotionEvent",
    "setByASN1ObjectArray",
    "SerializableCipher",
    "B",
    "TRIDENT",
    "BIT_STRING",
    "DERUTCTime",
    "pdf",
    "setValueOidString",
    "toUpperCase",
    "setByBigInteger",
    "shiftLeft",
    "fillStyle",
    "Date",
    "&browserVersion=",
    "complete",
    "Segoe UI Light",
    "keywords",
    "zVzcaQELjCrRYy7FeyUoJg",
    "xdid",
    "String",
    "fpflash.fraudmetrix.cn",
    "hasOwnProperty",
    "setMonth",
    " OPR/",
    "cqhk",
    "&errorType=",
    "i init ok",
    "kdf",
    "WEBOS",
    "zVzLaNELjKQSY3p2MrUWbF",
    "msBattery",
    "bin",
    "Helvetica",
    "description",
    "OBJECT_IDENTIFIER",
    "gen",
    "Wingdings 3",
    "Calibri",
    "compareTo",
    "className",
    "__proto__",
    "canSetSearchEngine",
    "number",
    "14px 'Arial'",
    "orientation",
    "StreamCipher",
    "onload",
    "jsonFreshUrl",
    "keyWords",
    "mac",
    "0101ff",
    "int",
    "A",
    "_sz",
    "lcvh",
    "_phantom",
    "Alipay",
    "Arial MT",
    "mousemove",
    "getPrivateBaseKeyB64",
    "zSHlknEgRLQIGZ7eeNUA",
    "Win32",
    "pBqF",
    "UTCTime",
    "MS Gothic",
    "Illegal character at offset ",
    "Courier",
    "substr",
    "UC",
    "/web3_7/profile.json",
    "CICy",
    "MS Serif",
    "LN2",
    "loaded",
    "=",
    "preview",
    "OpenSSL",
    "pDs5zKS6aO8GMWNHxO5X5pGCXNEa814Z7YdhtEpoaV2Kw5ebdlhbudxX6q8DD605",
    "JSON",
    "square",
    "zPHvawEejqPqY371eQUeJE",
    "zPzDIwOejChLGMpY",
    "cajaVersion",
    "UNSIGNED_BYTE",
    "_fmdata",
    "onmouseout",
    "z6HCanEGRVrRYy7FeyUoJg",
    "setASN1Object",
    "P",
    "})( +|$\n?)|(.{1,",
    "https://fp.tongdun.net",
    "fakeOut",
    "resize",
    "*",
    "getPrivateKeyB64",
    "touchpad",
    "Netscape",
    "DERNumericString",
    "Segoe Print",
    "_x64Fmix",
    "font-fingerprint-defender-alert",
    "addTo",
    "PrintableString",
    "Promise",
    "stack",
    "webdriver",
    "getMonth",
    "isOpera",
    "dAddOffset",
    "blackBoxType",
    ", ",
    "14",
    "safari",
    "01",
    "createBuffer",
    "\r\n-----END ",
    "HMAC",
    "find",
    "bot",
    "setByDate",
    "onclick",
    "Bookman Old Style",
    "Promise.race accepts an array",
    "hostname",
    "-",
    "[header:",
    "BOOLEAN",
    "spider",
    "startRendering",
    "prlt87lwxvm",
    "str",
    "zczwaMwFRIhrGZqbM4C6bF4t",
    "ltx71",
    "hPzQanwhjOPRiyplMaUeJq",
    "N",
    "03",
    "_counter",
    "cfg",
    "bbBB",
    "Gecko",
    "candidate",
    "t",
    "functionget",
    "true",
    "]",
    "1234567812345678",
    "h0HLaXEFjCQFGPple4U5bE",
    "zbHLa1EFjUPI",
    "findIndex",
    "https://fptest.fraudmetrix.cn/partnerDetect.json",
    "isEdge",
    "chargingTime",
    "queryUsageAndQuota",
    "onreadystatechange",
    "x509",
    "MD5",
    "In test[",
    "userAgent:",
    "attack",
    "cFcj",
    "ZERO",
    "toGMTString",
    "xor",
    "lqsJ",
    "_keySchedule",
    "decodeLength",
    "sub",
    "uc",
    "isPrototypeOf",
    "rGnj",
    "generate",
    "12",
    "iframe",
    "span",
    "outerHTML",
    "zRzLINEGRVQqY37bMQUo",
    "-9999px",
    "status",
    "&appName=",
    "on",
    "decode",
    "PasswordBasedCipher",
    "rgba(102, 204, 0, 0.7)",
    "default_public_exponent",
    "Application_",
    "fromRadix",
    "DERInteger",
    "MS Sans Serif",
    "_hash",
    "application/asx",
    "BfJy",
    "StyleMedia",
    "test",
    "chrome",
    "removeItem",
    "innerWidth",
    "InstallTrigger",
    "yrHe",
    "MYRIAD",
    "toHexDOM",
    "getHours",
    "</b>",
    "Hex",
    "open",
    "Arial Narrow",
    "bitCount",
    "__creator",
    "jTimeout",
    "hPzQIKwhjuhDiG7eeqUDJFxmz0HL",
    "fontSize",
    "Browser Plug",
    "getinfo",
    "toLocaleLowerCase",
    "setBit",
    "isGecko",
    "charging",
    "drawImage",
    "webos",
    "documentElement",
    "addHandler",
    " byte) ",
    "hexCurrent",
    "callSelenium",
    "MS PGothic",
    "bitLength",
    "facebookexternalhit",
    "imgLoaded",
    "i",
    "createOscillator",
    "title",
    "byteValue",
    "readyState",
    "2",
    "sigBytes",
    "e",
    "attrVertex",
    "MSPointerEvent",
    "remove",
    "text-rendering",
    "TRIANGLE_STRIP",
    "iePrivacy",
    "7",
    "mac os",
    "doPublic",
    "Image",
    "Hasher",
    "toRadix",
    "yangcong",
    "trident",
    "reverse",
    "ENUMERATED",
    "selected",
    "zeroPadding",
    "Geneva",
    "Chrome",
    "hexByte",
    "forEach",
    "createOffer",
    "reason",
    "channelCount",
    "private",
    "RGBA",
    "stream",
    "name2oidList",
    "removeChild",
    "rgba(255,255,255,1)",
    "isArray",
    "replace",
    "onmousemove",
    "alipay",
    "0123456789abcdef",
    "array",
    "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_",
    "DERIA5String",
    "durations",
    "~/=",
    "blackberry",
    "webkitRTCPeerConnection",
    "UCNewsJSController",
    "createShader",
    "miniprogram",
    "wr",
    "K",
    "toLowerCase",
    "Georgia",
    "name",
    "timer",
    "setDate",
    "node",
    "setByBooleanArray",
    "mfsG",
    "mpl",
    "pxy",
    "enDe",
    "edit",
    "reduction",
    "offsetWidth",
    "error",
    "application/vnd.chromium.remoting-viewer",
    "vertexAttribPointer",
    "ufHI",
    " hover",
    "02",
    "_k16",
    "getMinutes",
    "isIE",
    "hasher",
    "getKey",
    "audiocontext-fingerprint-defender-alert",
    "change",
    "getFullYear",
    "getElementsByTagName",
    "count",
    "typeName",
    "maxChannelCount",
    "divide",
    "sessionStorage",
    "idf",
    "iterations",
    "DV",
    "slice",
    "Safari",
    "no token returned",
    "ratio",
    "f736mgcni9c",
    "MS Outlook",
    "DERSet",
    "OPERA",
    "reliable",
    "ethernet",
    "id",
    "td_ua",
    "_keyStr",
    "Lucida Console",
    "unknown",
    "gdph",
    "Unrecognized time: ",
    "gcd",
    "GM_addResource",
    "application/gameplugin",
    "modInverse",
    "getFreshValueHex",
    "now",
    "bigIntToMinTwosComplementsHex",
    "0123456789abcdefghijklmnopqrstuvwxyz",
    "5",
    "false",
    "zNHQaIEGSLPwGq7AoHUJJdfj",
    "fullVersionList",
    "clamp",
    "decryptBlock",
    "asn1Array",
    "encrypt",
    "_fmBehaviorBlackbox",
    "compileShader",
    "isExplicit",
    "W",
    "webkitTemporaryStorage",
    "style",
    "dmp1",
    "mod",
    "standalone",
    "zNHpaKOkjLhIGZ7AMNCc",
    "setUnusedBitsAndHexValue",
    "TrackEvent",
    "z1HdawEcjuhiGPqYMQCpbKx9z0",
    "MSIE",
    "AudioContext",
    "hash128",
    "AES",
    "Possible Unhandled Promise Rejection:",
    "stringify",
    "vendor",
    "isUC",
    "onunload",
    "data",
    "zVzDIoOejKhIYyH1eTUabF",
    "ucapi",
    "shift",
    "sampleRate",
    "screen",
    "_Selenium_IDE_Recorder",
    "splice",
    "linux",
    "millerRabin",
    "tcpHost",
    "getParameter",
    "isSafari",
    "collectBehavior",
    "webkit",
    "log",
    "&",
    "Book Antiqua",
    "getTimezoneOffset",
    "taobao",
    "Opera",
    "check",
    "node collapsed",
    "TDpx",
    "script",
    "openDatabase",
    "quota",
    "v",
    "asn1Object",
    "language",
    "toDataURL",
    "get",
    "STATIC_DRAW",
    "all",
    "FLOAT",
    "checkStatus",
    "GeneralString",
    "words",
    " got ",
    "z1zjINELjGhLGP7A",
    "shortValue",
    "bingpreview",
    "Arial Rounded MT Bold",
    "promise",
    "IPHONE",
    "ipod",
    "getTime",
    "Console",
    "format",
    "Segoe Script",
    "Q",
    "Cambria Math",
    "frameElement",
    "numItems",
    "deleted",
    "zPHda1EGjlPIi37b",
    "UNMASKED_RENDERER_WEBGL",
    "fpHost",
    "hV",
    "app_name",
    "_callback=",
    "Apple",
    "h0HQaNwhjU",
    "; path=/",
    "-----BEGIN ",
    "detachEvent",
    "valueOf",
    "parseBitString",
    "Hex encoding incomplete: 4 bits missing",
    "toByteArray",
    "squareTo",
    "Lucida Sans Unicode",
    "Monaco",
    "_fmOpt",
    "ASN1Object",
    "Base64",
    "^^",
    "setValueName",
    "detectUrl",
    "PRESTO",
    "fromString",
    " on a stream of length ",
    "NumericString",
    "LIEBAO",
    "reSeemsASCII",
    "parseStringBMP",
    "formatDate",
    "setItem",
    "token_id",
    "itemSize",
    "getElementsByName",
    "src",
    "onicecandidate",
    "call",
    "mozilla",
    "setStringHex",
    "getUniformLocation",
    "dischargingTime",
    "callee",
    "0123456789ABCDEF",
    "htHdIwEFjzhiGM",
    "invoked",
    "getBattery",
    "print",
    "reTime",
    "getCookie"
]

# 混淆后的 JS
with open("p_study.js", "r", encoding="utf-8") as f:
    js_lines = f.readlines()

js = ""
for j in js_lines:
    js += j

for i in item:
    # Qo00o 需要根据你 fm_old.js 具体的字符串进行替换
    t=item.index(i)
    str_old = f"QQoQO0[{t}]"
    js = js.replace(str_old, '"' + i + '"')

# 还原后的 JS
with open("fm_new.js", "w", encoding="utf-8") as f:
    f.write(js)