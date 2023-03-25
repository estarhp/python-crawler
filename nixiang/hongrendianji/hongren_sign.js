let n={
    "no": "dy3020",
    "data": {
        "rankDay": "2022-07-03",
        "tag": "",
        "rankType": "直播传播指数榜"
    }
}



SHIFT=[
    24,
    16,
    8,
    0
]
blocks=[
    645095788,
    1950182242,
    1847928361,
    1077690182,
    1198220915,
    947086438,
    878077745,
    707476320,
    1801860462,
    1684808832,
    0,
    0,
    0,
    0,
    0,
    824,
    462868641,
    -1932844958,
    -1413619505,
    1817825362,
    -1507378532,
    131727222,
    -1168903150,
    1660408199,
    -2109982160,
    588637728,
    114863785,
    -167507155,
    1247417618,
    1059240146,
    469748939,
    -2094628973,
    2067732914,
    1976726698,
    -285557770,
    247490273,
    -2093935264,
    851663584,
    -592322930,
    606567141,
    173860960,
    -575355235,
    1186962907,
    494583048,
    -938249724,
    -1955484644,
    -1071733429,
    523203706,
    -1498679556,
    1883681771,
    1820046876,
    -90111818,
    -855685068,
    81918383,
    1502018522,
    -1979845954,
    785262795,
    -360201051,
    -810580662,
    -779458114,
    1119171965,
    -2052681144,
    -1327270922,
    -110044768
]
K=[
    1116352408,
    1899447441,
    3049323471,
    3921009573,
    961987163,
    1508970993,
    2453635748,
    2870763221,
    3624381080,
    310598401,
    607225278,
    1426881987,
    1925078388,
    2162078206,
    2614888103,
    3248222580,
    3835390401,
    4022224774,
    264347078,
    604807628,
    770255983,
    1249150122,
    1555081692,
    1996064986,
    2554220882,
    2821834349,
    2952996808,
    3210313671,
    3336571891,
    3584528711,
    113926993,
    338241895,
    666307205,
    773529912,
    1294757372,
    1396182291,
    1695183700,
    1986661051,
    2177026350,
    2456956037,
    2730485921,
    2820302411,
    3259730800,
    3345764771,
    3516065817,
    3600352804,
    4094571909,
    275423344,
    430227734,
    506948616,
    659060556,
    883997877,
    958139571,
    1322822218,
    1537002063,
    1747873779,
    1955562222,
    2024104815,
    2227730452,
    2361852424,
    2428436474,
    2756734187,
    3204031479,
    3329325298
]
EXTRA=[
    -2147483648,
    8388608,
    32768,
    128
]
HEX_CHARS=[
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "a",
    "b",
    "c",
    "d",
    "e",
    "f"
]
Sha256.prototype.finalize = function() {
                    if (!this.finalized) {
                        this.finalized = !0;
                        var t = this.blocks
                          , e = this.lastByteIndex;
                        t[16] = this.block,
                        t[e >> 2] |= EXTRA[3 & e],
                        this.block = t[16],
                        e >= 56 && (this.hashed || this.hash(),
                        t[0] = this.block,
                        t[16] = t[1] = t[2] = t[3] = t[4] = t[5] = t[6] = t[7] = t[8] = t[9] = t[10] = t[11] = t[12] = t[13] = t[14] = t[15] = 0),
                        t[14] = this.hBytes << 3 | this.bytes >>> 29,
                        t[15] = this.bytes << 3,
                        this.hash()
                    }
                }
Sha256.prototype.hex = function() {
                    this.finalize();
                    var t = this.h0
                      , e = this.h1
                      , n = this.h2
                      , i = this.h3
                      , r = this.h4
                      , o = this.h5
                      , a = this.h6
                      , s = this.h7
                      , l = HEX_CHARS[t >> 28 & 15] + HEX_CHARS[t >> 24 & 15] + HEX_CHARS[t >> 20 & 15] + HEX_CHARS[t >> 16 & 15] + HEX_CHARS[t >> 12 & 15] + HEX_CHARS[t >> 8 & 15] + HEX_CHARS[t >> 4 & 15] + HEX_CHARS[15 & t] + HEX_CHARS[e >> 28 & 15] + HEX_CHARS[e >> 24 & 15] + HEX_CHARS[e >> 20 & 15] + HEX_CHARS[e >> 16 & 15] + HEX_CHARS[e >> 12 & 15] + HEX_CHARS[e >> 8 & 15] + HEX_CHARS[e >> 4 & 15] + HEX_CHARS[15 & e] + HEX_CHARS[n >> 28 & 15] + HEX_CHARS[n >> 24 & 15] + HEX_CHARS[n >> 20 & 15] + HEX_CHARS[n >> 16 & 15] + HEX_CHARS[n >> 12 & 15] + HEX_CHARS[n >> 8 & 15] + HEX_CHARS[n >> 4 & 15] + HEX_CHARS[15 & n] + HEX_CHARS[i >> 28 & 15] + HEX_CHARS[i >> 24 & 15] + HEX_CHARS[i >> 20 & 15] + HEX_CHARS[i >> 16 & 15] + HEX_CHARS[i >> 12 & 15] + HEX_CHARS[i >> 8 & 15] + HEX_CHARS[i >> 4 & 15] + HEX_CHARS[15 & i] + HEX_CHARS[r >> 28 & 15] + HEX_CHARS[r >> 24 & 15] + HEX_CHARS[r >> 20 & 15] + HEX_CHARS[r >> 16 & 15] + HEX_CHARS[r >> 12 & 15] + HEX_CHARS[r >> 8 & 15] + HEX_CHARS[r >> 4 & 15] + HEX_CHARS[15 & r] + HEX_CHARS[o >> 28 & 15] + HEX_CHARS[o >> 24 & 15] + HEX_CHARS[o >> 20 & 15] + HEX_CHARS[o >> 16 & 15] + HEX_CHARS[o >> 12 & 15] + HEX_CHARS[o >> 8 & 15] + HEX_CHARS[o >> 4 & 15] + HEX_CHARS[15 & o] + HEX_CHARS[a >> 28 & 15] + HEX_CHARS[a >> 24 & 15] + HEX_CHARS[a >> 20 & 15] + HEX_CHARS[a >> 16 & 15] + HEX_CHARS[a >> 12 & 15] + HEX_CHARS[a >> 8 & 15] + HEX_CHARS[a >> 4 & 15] + HEX_CHARS[15 & a];
                    return this.is224 || (l += HEX_CHARS[s >> 28 & 15] + HEX_CHARS[s >> 24 & 15] + HEX_CHARS[s >> 20 & 15] + HEX_CHARS[s >> 16 & 15] + HEX_CHARS[s >> 12 & 15] + HEX_CHARS[s >> 8 & 15] + HEX_CHARS[s >> 4 & 15] + HEX_CHARS[15 & s]),
                    l
                }
function Sha256(t, e) {
e ? (blocks[0] = blocks[16] = blocks[1] = blocks[2] = blocks[3] = blocks[4] = blocks[5] = blocks[6] = blocks[7] = blocks[8] = blocks[9] = blocks[10] = blocks[11] = blocks[12] = blocks[13] = blocks[14] = blocks[15] = 0,
this.blocks = blocks) : this.blocks = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
t ? (this.h0 = 3238371032,
this.h1 = 914150663,
this.h2 = 812702999,
this.h3 = 4144912697,
this.h4 = 4290775857,
this.h5 = 1750603025,
this.h6 = 1694076839,
this.h7 = 3204075428) : (this.h0 = 1779033703,
this.h1 = 3144134277,
this.h2 = 1013904242,
this.h3 = 2773480762,
this.h4 = 1359893119,
this.h5 = 2600822924,
this.h6 = 528734635,
this.h7 = 1541459225),
this.block = this.start = this.bytes = this.hBytes = 0,
this.finalized = this.hashed = !1,
this.first = !0,
this.is224 = t
}
Sha256.prototype.hash = function() {
                    var t, e, n, i, r, o, a, s, l, u, c, h = this.h0, f = this.h1, d = this.h2, p = this.h3, g = this.h4, v = this.h5, m = this.h6, y = this.h7, x = this.blocks;
                    for (t = 16; t < 64; ++t)
                        r = x[t - 15],
                        e = (r >>> 7 | r << 25) ^ (r >>> 18 | r << 14) ^ r >>> 3,
                        r = x[t - 2],
                        n = (r >>> 17 | r << 15) ^ (r >>> 19 | r << 13) ^ r >>> 10,
                        x[t] = x[t - 16] + e + x[t - 7] + n << 0;
                    for (c = f & d,
                    t = 0; t < 64; t += 4)
                        this.first ? (this.is224 ? (s = 300032,
                        r = x[0] - 1413257819,
                        y = r - 150054599 << 0,
                        p = r + 24177077 << 0) : (s = 704751109,
                        r = x[0] - 210244248,
                        y = r - 1521486534 << 0,
                        p = r + 143694565 << 0),
                        this.first = !1) : (e = (h >>> 2 | h << 30) ^ (h >>> 13 | h << 19) ^ (h >>> 22 | h << 10),
                        n = (g >>> 6 | g << 26) ^ (g >>> 11 | g << 21) ^ (g >>> 25 | g << 7),
                        s = h & f,
                        i = s ^ h & d ^ c,
                        a = g & v ^ ~g & m,
                        r = y + n + a + K[t] + x[t],
                        o = e + i,
                        y = p + r << 0,
                        p = r + o << 0),
                        e = (p >>> 2 | p << 30) ^ (p >>> 13 | p << 19) ^ (p >>> 22 | p << 10),
                        n = (y >>> 6 | y << 26) ^ (y >>> 11 | y << 21) ^ (y >>> 25 | y << 7),
                        l = p & h,
                        i = l ^ p & f ^ s,
                        a = y & g ^ ~y & v,
                        r = m + n + a + K[t + 1] + x[t + 1],
                        o = e + i,
                        m = d + r << 0,
                        d = r + o << 0,
                        e = (d >>> 2 | d << 30) ^ (d >>> 13 | d << 19) ^ (d >>> 22 | d << 10),
                        n = (m >>> 6 | m << 26) ^ (m >>> 11 | m << 21) ^ (m >>> 25 | m << 7),
                        u = d & p,
                        i = u ^ d & h ^ l,
                        a = m & y ^ ~m & g,
                        r = v + n + a + K[t + 2] + x[t + 2],
                        o = e + i,
                        v = f + r << 0,
                        f = r + o << 0,
                        e = (f >>> 2 | f << 30) ^ (f >>> 13 | f << 19) ^ (f >>> 22 | f << 10),
                        n = (v >>> 6 | v << 26) ^ (v >>> 11 | v << 21) ^ (v >>> 25 | v << 7),
                        c = f & d,
                        i = c ^ f & p ^ u,
                        a = v & m ^ ~v & y,
                        r = g + n + a + K[t + 3] + x[t + 3],
                        o = e + i,
                        g = h + r << 0,
                        h = r + o << 0;
                    this.h0 = this.h0 + h << 0,
                    this.h1 = this.h1 + f << 0,
                    this.h2 = this.h2 + d << 0,
                    this.h3 = this.h3 + p << 0,
                    this.h4 = this.h4 + g << 0,
                    this.h5 = this.h5 + v << 0,
                    this.h6 = this.h6 + m << 0,
                    this.h7 = this.h7 + y << 0
                }
Sha256.prototype.update = function(t) {
                    if (!this.finalized) {
                        var e, n = typeof t;
                        if ("string" !== n) {
                            if ("object" !== n)
                                throw new Error(ERROR);
                            if (null === t)
                                throw new Error(ERROR);
                            if (ARRAY_BUFFER && t.constructor === ArrayBuffer)
                                t = new Uint8Array(t);
                            else if (!Array.isArray(t) && (!ARRAY_BUFFER || !ArrayBuffer.isView(t)))
                                throw new Error(ERROR);
                            e = !0
                        }
                        var i, r, o = 0, a = t.length, s = this.blocks;
                        while (o < a) {
                            if (this.hashed && (this.hashed = !1,
                            s[0] = this.block,
                            s[16] = s[1] = s[2] = s[3] = s[4] = s[5] = s[6] = s[7] = s[8] = s[9] = s[10] = s[11] = s[12] = s[13] = s[14] = s[15] = 0),
                            e)
                                for (r = this.start; o < a && r < 64; ++o)
                                    s[r >> 2] |= t[o] << SHIFT[3 & r++];
                            else
                                for (r = this.start; o < a && r < 64; ++o)
                                    i = t.charCodeAt(o),
                                    i < 128 ? s[r >> 2] |= i << SHIFT[3 & r++] : i < 2048 ? (s[r >> 2] |= (192 | i >> 6) << SHIFT[3 & r++],
                                    s[r >> 2] |= (128 | 63 & i) << SHIFT[3 & r++]) : i < 55296 || i >= 57344 ? (s[r >> 2] |= (224 | i >> 12) << SHIFT[3 & r++],
                                    s[r >> 2] |= (128 | i >> 6 & 63) << SHIFT[3 & r++],
                                    s[r >> 2] |= (128 | 63 & i) << SHIFT[3 & r++]) : (i = 65536 + ((1023 & i) << 10 | 1023 & t.charCodeAt(++o)),
                                    s[r >> 2] |= (240 | i >> 18) << SHIFT[3 & r++],
                                    s[r >> 2] |= (128 | i >> 12 & 63) << SHIFT[3 & r++],
                                    s[r >> 2] |= (128 | i >> 6 & 63) << SHIFT[3 & r++],
                                    s[r >> 2] |= (128 | 63 & i) << SHIFT[3 & r++]);
                            this.lastByteIndex = r,
                            this.bytes += r - this.start,
                            r >= 64 ? (this.block = s[16],
                            this.start = r - 64,
                            this.hash(),
                            this.hashed = !0) : this.start = r
                        }
                        return this.bytes > 4294967295 && (this.hBytes += this.bytes / 4294967296 << 0,
                        this.bytes = this.bytes % 4294967296),
                        this
                    }
                }
function E(n, e) {
    return k("param=" + JSON.stringify(n) + "&timestamp=" + e + "&tenant=1&salt=" + 'kbn%&)@<?FGkfs8sdf4Vg1*+;`kf5ndl$')
        }
function k(n) {
                        return new Sha256(undefined,!0).update(n)['hex']()
                    }


function main(token) {
    let e=1670569841092


    sign=E(n,e)
    data={
      "param": "{\"no\":\"dy3020\",\"data\":{\"rankDay\":\"2022-07-03\",\"tag\":\"\",\"rankType\":\"直播传播指数榜\"}}",
      "sign": sign,
      "tenant": "1",
      "timestamp": e,
      "token": token
}
    console.log(data)
    return data


                    }
                    main("YYcoki1/8BEQUIiyLfNHVIa1uw3hQc6/qrs8nOX/nhArHuAuGTEFng==")
