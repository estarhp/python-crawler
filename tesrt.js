const  CryptoJS = require("crypto-js")
const  RSA = require("rsa-javascript")
  j2x={}


    var Hb3x = function(i2x, t2x) {
        try {
            t2x = t2x.toLowerCase();
            if (i2x === null)
                return t2x == "null";
            if (i2x === undefined)
                return t2x == "undefined";
            return bd2x.toString.call(i2x).toLowerCase() == "[object " + t2x + "]"
        } catch (e) {
            return !1
        }
    };
    j2x.gV4Z = function(i2x) {
        return Hb3x(i2x, "function")
    }
    ;
    j2x.fO4S = function(i2x) {
        return Hb3x(i2x, "string")
    }
    ;
    j2x.tT9K = function(i2x) {
        return Hb3x(i2x, "number")
    }
    ;
    j2x.cMf6Z = function(i2x) {
        return Hb3x(i2x, "boolean")
    }
    ;
    j2x.DK2x = function(i2x) {
        return Hb3x(i2x, "date")
    }
    ;
    j2x.ec3x = function(i2x) {
        return Hb3x(i2x, "array")
    }
    ;
    j2x.mi6c = function(i2x) {
        return Hb3x(i2x, "object")
    }
    ;
    j2x.fS4W = function() {
        var do3x = /[^\x00-\xfff]/g;
        return function(bq2x) {
            return ("" + (bq2x || "")).replace(do3x, "**").length
        }
    }();
    j2x.dx3x = function(k2x, q2x) {
        var eh3x = j2x.gV4Z(q2x) ? q2x : function(D2x) {
            return D2x === q2x
        }
          , r2x = j2x.eV3x(k2x, eh3x);
        return r2x != null ? r2x : -1
    }
    ;
    j2x.cMe6Y = function() {
        var bEG8y;
        var VE0x = function(k2x, pT7M, qe8W) {
            if (pT7M > qe8W)
                return -1;
            var Is6m = Math.ceil((pT7M + qe8W) / 2)
              , m2x = bEG8y(k2x[Is6m], Is6m, k2x);
            if (m2x == 0)
                return Is6m;
            if (m2x < 0)
                return VE0x(k2x, pT7M, Is6m - 1);
            return VE0x(k2x, Is6m + 1, qe8W)
        };
        return function(k2x, Mp8h) {
            bEG8y = Mp8h || bs2x;
            return VE0x(k2x, 0, k2x.length - 1)
        }
    }();
    j2x.ox7q = function(k2x, cH3x, O2x) {
        if (!k2x || !k2x.length || !j2x.gV4Z(cH3x))
            return null;
        for (var i = k2x.length - 1; i >= 0; i--)
            if (!!cH3x.call(O2x, k2x[i], i, k2x))
                return i;
        return null
    }
    ;
    j2x.bg2x = function(k2x, cH3x, O2x) {
        if (!k2x || !k2x.length || !j2x.gV4Z(cH3x))
            return this;
        if (!!k2x.forEach) {
            k2x.forEach(cH3x, O2x);
            return this
        }
        for (var i = 0, l = k2x.length; i < l; i++)
            cH3x.call(O2x, k2x[i], i, k2x);
        return this
    }
    ;
    j2x.eV3x = function(k2x, cH3x, O2x) {
        if (!k2x || !j2x.gV4Z(cH3x))
            return null;
        if (k2x.length != null) {
            if (k2x.length > 0)
                for (var i = 0, l = k2x.length; i < l; i++)
                    if (!!cH3x.call(O2x, k2x[i], i, k2x))
                        return i
        }
        if (j2x.mi6c(k2x)) {
            for (var x in k2x)
                if (k2x.hasOwnProperty(x) && !!cH3x.call(O2x, k2x[x], x, k2x))
                    return x
        }
        return null
    }
    ;
    j2x.cCY4c = function(jI5N, cDg4k, e2x) {
        jI5N = jI5N || [];
        e2x = e2x || bd2x;
        var bEL8D = !!e2x.union
          , yJ0x = !!e2x.begin
          , bbj1x = e2x.compare
          , cDq4u = bEL8D && yJ0x ? j2x.ox7q : j2x.bg2x;
        cDq4u(cDg4k, function(q2x) {
            if (!!bbj1x)
                bbj1x = bbj1x.eP3x(q2x);
            var r2x = j2x.dx3x(jI5N, bbj1x || q2x);
            if (r2x >= 0)
                jI5N.splice(r2x, 1);
            if (bEL8D)
                jI5N[yJ0x ? "unshift" : "push"](q2x)
        });
        return jI5N
    }
    ;
    j2x.Dz2x = function(bD2x, bq2x) {
        if (!bD2x || !bq2x || !bq2x.replace)
            return bq2x || "";
        return bq2x.replace(bD2x.r, function($1) {
            var m2x = bD2x[!bD2x.i ? $1.toLowerCase() : $1];
            return m2x != null ? m2x : $1
        })
    }
    ;
    j2x.dN3x = function() {
        var bD2x = {
            r: /\<|\>|\&lt;|\&gt;|\&|\r|\n|\s|\'|\"/g,
            "<": "&lt;",
            ">": "&gt;",
            "&": "&amp;",
            " ": "&nbsp;",
            '"': "&quot;",
            "'": "&#39;",
            "\n": "<br/>",
            "\r": "",
            "&lt;": "&lt;",
            "&gt;": "&gt;"
        };
        return function(bq2x) {
            return j2x.Dz2x(bD2x, bq2x)
        }
    }();
    j2x.AD1x = function() {
        var bD2x = {
            r: /\&(?:lt|gt|amp|nbsp|#39|quot)\;|\<br\/\>/gi,
            "&lt;": "<",
            "&gt;": ">",
            "&amp;": "&",
            "&nbsp;": " ",
            "&#39;": "'",
            "&quot;": '"',
            "<br/>": "\n"
        };
        return function(bq2x) {
            return j2x.Dz2x(bD2x, bq2x)
        }
    }();
    j2x.id5i = function() {
        var bD2x = {
            i: !0,
            r: /\byyyy|yy|MM|cM|eM|M|dd|d|HH|H|mm|ms|ss|m|s|w|ct|et\b/g
        }
          , cDM4Q = ["上午", "下午"]
          , cDQ4U = ["A.M.", "P.M."]
          , blr3x = ["日", "一", "二", "三", "四", "五", "六"]
          , cDX4b = ["一", "二", "三", "四", "五", "六", "七", "八", "九", "十", "十一", "十二"]
          , cEr5w = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sept", "Oct", "Nov", "Dec"];
        var Vj0x = function(ht4x) {
            ht4x = parseInt(ht4x) || 0;
            return (ht4x < 10 ? "0" : "") + ht4x
        };
        var cEF5K = function(qJ8B) {
            return qJ8B < 12 ? 0 : 1
        };
        return function(bz2x, KK7D, cEK5P) {
            if (!bz2x || !KK7D)
                return "";
            bz2x = j2x.baI1x(bz2x);
            bD2x.yyyy = bz2x.getFullYear();
            bD2x.yy = ("" + bD2x.yyyy).substr(2);
            bD2x.M = bz2x.getMonth() + 1;
            bD2x.MM = Vj0x(bD2x.M);
            bD2x.eM = cEr5w[bD2x.M - 1];
            bD2x.cM = cDX4b[bD2x.M - 1];
            bD2x.d = bz2x.getDate();
            bD2x.dd = Vj0x(bD2x.d);
            bD2x.H = bz2x.getHours();
            bD2x.HH = Vj0x(bD2x.H);
            bD2x.m = bz2x.getMinutes();
            bD2x.mm = Vj0x(bD2x.m);
            bD2x.s = bz2x.getSeconds();
            bD2x.ss = Vj0x(bD2x.s);
            bD2x.ms = bz2x.getMilliseconds();
            bD2x.w = blr3x[bz2x.getDay()];
            var bEY8Q = cEF5K(bD2x.H);
            bD2x.ct = cDM4Q[bEY8Q];
            bD2x.et = cDQ4U[bEY8Q];
            if (!!cEK5P) {
                bD2x.H = bD2x.H % 12
            }
            return j2x.Dz2x(bD2x, KK7D)
        }
    }();
    j2x.baI1x = function(bz2x) {
        var dj3x = bz2x;
        if (j2x.fO4S(bz2x))
            dj3x = new Date(Date.parse(bz2x));
        if (!j2x.DK2x(bz2x))
            dj3x = new Date(bz2x);
        return dj3x
    }
    ;
    j2x.Or8j = function(cFY5d, cGx5C) {
        return (new Number(cFY5d)).toFixed(cGx5C)
    }
    ;
    j2x.bof4j = function() {
        var hd4h = /([^\/:])\/.*$/
          , kG5L = /\/[^\/]+$/
          , FC2x = /[#\?]/
          , bos4w = 'https://music.163.com/'
        var bow4A = function(jE5J) {
            return (jE5J || "").indexOf("://") > 0
        };
        var bFa8S = function(jE5J) {
            return (jE5J || "").split(FC2x)[0].replace(kG5L, "/")
        };
        var cGY5d = function(jE5J, gv4z) {
            if (jE5J.indexOf("/") == 0)
                return gv4z.replace(hd4h, "$1") + jE5J;
            return bFa8S(gv4z) + jE5J
        };
        bos4w = bFa8S(bos4w);
        return function(jE5J, gv4z) {
            jE5J = (jE5J || "").trim();
            if (!bow4A(gv4z))
                gv4z = bos4w;
            if (!jE5J)
                return gv4z;
            if (bow4A(jE5J))
                return jE5J;
            jE5J = cGY5d(jE5J, gv4z);
            uf9W.href = jE5J;
            jE5J = uf9W.href;
            return bow4A(jE5J) ? jE5J : uf9W.getAttribute("href", 4)
        }
    }();
    j2x.cHR5W = function() {
        var do3x = /^([\w]+?:\/\/.*?(?=\/|$))/i;
        return function(Y2x) {
            if (do3x.test(Y2x || ""))
                return RegExp.$1.toLowerCase();
            return ""
        }
    }();
    j2x.bFd8V = function(K2x, iE5J) {
        if (!K2x)
            return iE5J;
        var Z2x = K2x.tagName.toLowerCase()
          , k2x = a1x.di3x(K2x);
        if (!k2x || !k2x.length) {
            iE5J[Z2x] = K2x.textContent || K2x.text || "";
            return iE5J
        }
        var cl3x = {};
        iE5J[Z2x] = cl3x;
        j2x.bg2x(k2x, function(g2x) {
            j2x.bFd8V(g2x, cl3x)
        });
        return iE5J
    }
    ;
    j2x.cKZ6T = function(Fh2x) {
        try {
            return j2x.bFd8V(a1x.bEo8g(Fh2x), {})
        } catch (ex) {
            return null
        }
    }
    ;
    j2x.UR0x = function(iu5z, UP0x) {
        var iE5J = {};
        j2x.bg2x((iu5z || "").split(UP0x), function(Z2x) {
            var bad1x = Z2x.split("=");
            if (!bad1x || !bad1x.length)
                return;
            var J2x = bad1x.shift();
            if (!J2x)
                return;
            iE5J[decodeURIComponent(J2x)] = decodeURIComponent(bad1x.join("="))
        });
        return iE5J
    }
    ;
    j2x.wf0x = function(gG4K, UP0x, cKV6P) {
        if (!gG4K)
            return "";
        var bx2x = [];
        for (var x in gG4K) {
            bx2x.push(encodeURIComponent(x) + "=" + (!!cKV6P ? encodeURIComponent(gG4K[x]) : gG4K[x]))
        }
        return bx2x.join(UP0x || ",")
    }
    ;
    j2x.hg4k = function(bv2x) {
        return j2x.UR0x(bv2x, "&")
    }
    ;
    j2x.cr3x = function(gG4K) {
        return j2x.wf0x(gG4K, "&", !0)
    }
    ;
    j2x.cKX6R = function(gG4K) {
        return bl2x.KS7L(gG4K)
    }
    ;
    j2x.cNN6H = function(k2x, eh3x) {
        var m2x = {};
        j2x.bg2x(k2x, function(q2x) {
            var J2x = q2x;
            if (!!eh3x) {
                J2x = eh3x(q2x)
            }
            m2x[J2x] = q2x
        });
        return m2x
    }
    ;
    j2x.cKY6S = function(ht4x, gq4u) {
        var cKQ6K = ("" + ht4x).length
          , cKN6H = Math.max(1, parseInt(gq4u) || 0)
          , dA3x = cKN6H - cKQ6K;
        if (dA3x > 0) {
            ht4x = (new Array(dA3x + 1)).join("0") + ht4x
        }
        return "" + ht4x
    }
    ;
    j2x.ZT1x = function(gG4K, Z2x) {
        if (!j2x.ec3x(Z2x)) {
            try {
                delete gG4K[Z2x]
            } catch (e) {
                gG4K[Z2x] = undefined
            }
            return this
        }
        j2x.bg2x(Z2x, j2x.ZT1x.f2x(j2x, gG4K));
        return this
    }
    ;
    j2x.WS0x = function() {
        var bFp8h = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXTZabcdefghiklmnopqrstuvwxyz";
        return function(bt2x) {
            bt2x = bt2x || 10;
            var m2x = [];
            for (var i = 0, bFs9j; i < bt2x; ++i) {
                bFs9j = Math.floor(Math.random() * bFp8h.length);
                m2x.push(bFp8h.charAt(bFs9j))
            }
            return m2x.join("")
        }
    }();
    j2x.CV2x = function(fU4Y, fB4F) {
        return Math.floor(Math.random() * (fB4F - fU4Y) + fU4Y)
    }
    ;
    j2x.oQ7J = function(bt2x) {
        bt2x = Math.max(0, Math.min(bt2x || 8, 30));
        var fU4Y = Math.pow(10, bt2x - 1)
          , fB4F = fU4Y * 10;
        return j2x.CV2x(fU4Y, fB4F).toString()
    }
    ;
    j2x.btF6z = function(bJ2x) {
        return Object.assign(bJ2x, {
            result: Object.assign(bJ2x.playlist, {
                tracks: bJ2x.playlist.tracks.map(function(track) {
                    return Object.assign(track, {
                        album: track.al,
                        artists: track.ar,
                        position: track.no,
                        duration: track.dt,
                        disc: track.cd,
                        popularity: track.pop,
                        mvid: track.mv,
                        lMusic: track.l ? {
                            bitrate: track.l.br,
                            volumeDelta: track.l.vd,
                            size: track.l.size,
                            dfsId: track.l.fid
                        } : {},
                        mMusic: track.m ? {
                            bitrate: track.m.br,
                            volumeDelta: track.m.vd,
                            size: track.m.size,
                            dfsId: track.m.fid
                        } : {},
                        hMusic: track.h ? {
                            bitrate: track.h.br,
                            volumeDelta: track.h.vd,
                            size: track.h.size,
                            dfsId: track.h.fid
                        } : {}
                    })
                })
            })
        })
    }
    ;
    j2x.ZK1x = function() {
        var hh4l = +(new Date);
        return function() {
            return "" + hh4l++
        }
    }()
window = {}


 window.NEJ = window.NEJ || {};
NEJ=window.NEJ
NEJ.O = {};
    NEJ.R = [];
    NEJ.F = function() {
        return !1
    }
    ;
    NEJ.P = function(GI3x) {
        if (!GI3x || !GI3x.length)
            return null;
        var ZF1x = window;
        for (var a = GI3x.split("."), l = a.length, i = a[0] == "window" ? 1 : 0; i < l; ZF1x = ZF1x[a[i]] = ZF1x[a[i]] || {},
        i++)
            ;
        return ZF1x
    }




    window.GEnc = true;
    var bsi5n = function(cxK3x) {
        var m2x = [];
        j2x.bg2x(cxK3x, function(cxJ3x) {
            m2x.push(Vx0x.emj[cxJ3x])
        });
        return m2x.join("")
    };

function a(a) {
        var d, e, b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", c = "";
        for (d = 0; a > d; d += 1)
            e = Math.random() * b.length,
            e = Math.floor(e),
            c += b.charAt(e);
        return c
    }

    function b(a, b) {
        var c = CryptoJS.enc.Utf8.parse(b)
          , d = CryptoJS.enc.Utf8.parse("0102030405060708")
          , e = CryptoJS.enc.Utf8.parse(a)
          , f = CryptoJS.AES.encrypt(e, c, {
            iv: d,
            mode: CryptoJS.mode.CBC
        });
        return f.toString()
    }
    function c(a, b, c) {
        var d, e;
        return RSA.setMaxDigits(131),
        d = new RSA.RSAKeyPair(b,"",c),
        e = RSA.encryptedString(d, a)
    }

function d(d, e, f, g) {
        var h = {}
          , i = a(16);
        return h.encText = b(d, g),
        h.encText = b(h.encText, i),
        h.encSecKey = c(i, e, f),
        h
    }

    function e(a, b, d, e) {
        var f = {};
        return f.encText = c(a + e, b, d),
        f
    }


let i2x = {
    "rid": "R_SO_4_26243686",
    "threadId": "R_SO_4_26243686",
    "pageNo": "3",
    "pageSize": "20",
    "cursor": "1683825609731",
    "offset": "0",
    "orderType": "1",
    "csrf_token": "154c4129b78f478464f1a79022ab11d5"
}



console.log(d(JSON.stringify(i2x), '010001', '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7', '0CoJUm6Qyw8W8jud'))

