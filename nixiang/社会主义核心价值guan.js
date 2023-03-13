
o = function(t) {
        var n = /[A-Za-z0-9\-\_\.\!\~\*\'\(\)]/g
          , r = t.replace(n, function(t) {
            return t.codePointAt(0).toString(16)
        });
        return encodeURIComponent(r).replace(/%/g, "").toUpperCase()
    }




var h="富强民主文明和谐自由平等公正法治爱国敬业诚信友善"


var e = function() {
        for (var t = arguments.length, n = Array(t), r = 0; r < t; r++)
            n[r] = arguments[r];
        var e = n.length
          , i = "string" == typeof n[e - 1] ? n[e - 1] : "Assert Error"
          , o = !0
          , u = !1
          , c = void 0;
        try {
            for (var f, a = n[Symbol.iterator](); !(o = (f = a.next()).done); o = !0) {
                if (!f.value)
                    throw new Error(i)
            }
        } catch (t) {
            u = !0,
            c = t
        } finally {
            try {
                !o && a.return && a.return()
            } finally {
                if (u)
                    throw c
            }
        }
    }

var i = function() {
        return Math.random() >= .5
    }

c = function(t) {
        e("string" == typeof t);
        var n = []
          , r = !0
          , o = !1
          , u = void 0;

            for (var c, f = t[Symbol.iterator](); !(r = (c = f.next()).done); r = !0) {
                var a = c.value
                  , s = Number.parseInt(a, 16);
                s < 10 ? n.push(s) : i() ? (n.push(10),
                n.push(s - 10)) : (n.push(11),
                n.push(s - 6))
            }

        return n
    }
a = function(t) {
        return t.map(function(t) {
            return h[2 * t] + h[2 * t + 1]
        }).join("")
    }




console.log(a(c(o("今天是瓜熙熙"))))