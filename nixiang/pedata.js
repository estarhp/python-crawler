var zlib = require('zlib');

function B(e, t) {
                if ("1" == t)
                    return [7, 65, 75, 31, 71, 101, 57, 0];
                for (var n = [], i = 0, a = t.length; i < a; i += 2)
                    n.push(e.substr(1 * t.substr(i, 2), 1).charCodeAt());
                return n
            }

function F(e, t) {
                for (var n, i = new Uint8Array(e.length), a = 0, s = e.length; a < s; a++)
                    n = t[a % t.length],
                    i[a] = e[a].charCodeAt() ^ n;
                return i
            }

function Y(t, n) {
                var i = B('fc8bdffcd745cc1b8556a8868469a55b91161b4b74f2c579017e2a606481d6cc', n)
                  , a = F(V(t), i)




// Declaring input and assigning
// it a value string
var input = "Nidhi";

// Calling gzipSync method


// Calling gunzipSync method
var decom = zlib.gunzipSync(
new Buffer.from(a)).toString();



return JSON.parse(decom)
            }

function V(e) {
                var t, n, i, a, s, r, o, c = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=", u = "", l = 0;
                e = e.replace(/[^A-Za-z0-9\+\/\=]/g, "");
                while (l < e.length)
                    a = c.indexOf(e.charAt(l++)),
                    s = c.indexOf(e.charAt(l++)),
                    r = c.indexOf(e.charAt(l++)),
                    o = c.indexOf(e.charAt(l++)),
                    t = a << 2 | s >> 4,
                    n = (15 & s) << 4 | r >> 2,
                    i = (3 & r) << 6 | o,
                    u += String.fromCharCode(t),
                    64 != r && (u += String.fromCharCode(n)),
                    64 != o && (u += String.fromCharCode(i));
                return u
            }







console.log(Y("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"
,"6314220260351805"))