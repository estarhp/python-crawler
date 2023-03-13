z = function(e) {
            var t, n = [];
            if (void 0 === e)
                return "";
            t = function(e) {
                for (var t, n = e.toString(), r = [], o = 0; o < n.length; o++)
                    0 <= (t = n.charCodeAt(o)) && t <= 127 ? r.push(t) : 128 <= t && t <= 2047 ? (r.push(192 | 31 & t >> 6),
                    r.push(128 | 63 & t)) : (2048 <= t && t <= 55295 || 57344 <= t && t <= 65535) && (r.push(224 | 15 & t >> 12),
                    r.push(128 | 63 & t >> 6),
                    r.push(128 | 63 & t));
                for (var i = 0; i < r.length; i++)
                    r[i] &= 255;
                return r
            }(e);
            for (var r = 0, o = t.length; r < o; ++r)
                n.push((5 ^ t[r]).toString(16));
            return n.join("")
        }


