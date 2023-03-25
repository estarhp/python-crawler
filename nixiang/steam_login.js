// /**** (c) Valve Corporation. Use is governed by the terms of the Steam Subscriber Agreement http://store.steampowered.com/subscriber_agreement/.
// ****/
//
// navigator={
//     userAgent: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
// }
// function a(t) {
//             return "0123456789abcdefghijklmnopqrstuvwxyz".charAt(t)
//         }
//         function u(t, r) {
//             var e = c[t.charCodeAt(r)];
//             return null == e ? -1 : e
//         }
//         function f(t) {
//             var r = s();
//             return r.fromInt(t),
//             r
//         }
//         function l(t) {
//             var r, e = 1;
//             return 0 != (r = t >>> 16) && (t = r,
//             e += 16),
//             0 != (r = t >> 8) && (t = r,
//             e += 8),
//             0 != (r = t >> 4) && (t = r,
//             e += 4),
//             0 != (r = t >> 2) && (t = r,
//             e += 2),
//             0 != (r = t >> 1) && (t = r,
//             e += 1),
//             e
//         }
//         function p(t) {
//             this.m = t
//         }
//         function b(t) {
//             this.m = t,
//             this.mp = t.invDigit(),
//             this.mpl = 32767 & this.mp,
//             this.mph = this.mp >> 15,
//             this.um = (1 << t.DB - 15) - 1,
//             this.mt2 = 2 * t.t
//         }
//         function m(t, r) {
//             return t & r
//         }
//         function d(t, r) {
//             return t | r
//         }
//         function T(t, r) {
//             return t ^ r
//         }
//         function v(t, r) {
//             return t & ~r
//         }
//         function y(t) {
//             if (0 == t)
//                 return -1;
//             var r = 0;
//             return 0 == (65535 & t) && (t >>= 16,
//             r += 16),
//             0 == (255 & t) && (t >>= 8,
//             r += 8),
//             0 == (15 & t) && (t >>= 4,
//             r += 4),
//             0 == (3 & t) && (t >>= 2,
//             r += 2),
//             0 == (1 & t) && ++r,
//             r
//         }
//         function g(t) {
//             for (var r = 0; 0 != t; )
//                 t &= t - 1,
//                 ++r;
//             return r
//         }
//         function _() {}
//         function k(t) {
//             return t
//         }
//
// i.prototype.copyTo = function(t) {
//             for (var r = this.t - 1; r >= 0; --r)
//                 t[r] = this[r];
//             t.t = this.t,
//             t.s = this.s
//         }
//         ,
//         i.prototype.fromInt = function(t) {
//             this.t = 1,
//             this.s = t < 0 ? -1 : 0,
//             t > 0 ? this[0] = t : t < -1 ? this[0] = t + DV : this.t = 0
//         }
//         ,
//         i.prototype.fromString = function(t, r) {
//             var e;
//             if (16 == r)
//                 e = 4;
//             else if (8 == r)
//                 e = 3;
//             else if (256 == r)
//                 e = 8;
//             else if (2 == r)
//                 e = 1;
//             else if (32 == r)
//                 e = 5;
//             else {
//                 if (4 != r)
//                     return void this.fromRadix(t, r);
//                 e = 2
//             }
//             this.t = 0,
//             this.s = 0;
//             for (var o = t.length, s = !1, n = 0; --o >= 0; ) {
//                 var h = 8 == e ? 255 & t[o] : u(t, o);
//                 h < 0 ? "-" == t.charAt(o) && (s = !0) : (s = !1,
//                 0 == n ? this[this.t++] = h : n + e > this.DB ? (this[this.t - 1] |= (h & (1 << this.DB - n) - 1) << n,
//                 this[this.t++] = h >> this.DB - n) : this[this.t - 1] |= h << n,
//                 (n += e) >= this.DB && (n -= this.DB))
//             }
//             8 == e && 0 != (128 & t[0]) && (this.s = -1,
//             n > 0 && (this[this.t - 1] |= (1 << this.DB - n) - 1 << n)),
//             this.clamp(),
//             s && i.ZERO.subTo(this, this)
//         }
//         ,
//         i.prototype.clamp = function() {
//             for (var t = this.s & this.DM; this.t > 0 && this[this.t - 1] == t; )
//                 --this.t
//         }
//         ,
//         i.prototype.dlShiftTo = function(t, r) {
//             var e;
//             for (e = this.t - 1; e >= 0; --e)
//                 r[e + t] = this[e];
//             for (e = t - 1; e >= 0; --e)
//                 r[e] = 0;
//             r.t = this.t + t,
//             r.s = this.s
//         }
//         ,
//         i.prototype.drShiftTo = function(t, r) {
//             for (var e = t; e < this.t; ++e)
//                 r[e - t] = this[e];
//             r.t = Math.max(this.t - t, 0),
//             r.s = this.s
//         }
//         ,
//         i.prototype.lShiftTo = function(t, r) {
//             var e, o = t % this.DB, i = this.DB - o, s = (1 << i) - 1, n = Math.floor(t / this.DB), h = this.s << o & this.DM;
//             for (e = this.t - 1; e >= 0; --e)
//                 r[e + n + 1] = this[e] >> i | h,
//                 h = (this[e] & s) << o;
//             for (e = n - 1; e >= 0; --e)
//                 r[e] = 0;
//             r[n] = h,
//             r.t = this.t + n + 1,
//             r.s = this.s,
//             r.clamp()
//         }
//         ,
//         i.prototype.rShiftTo = function(t, r) {
//             r.s = this.s;
//             var e = Math.floor(t / this.DB);
//             if (e >= this.t)
//                 r.t = 0;
//             else {
//                 var o = t % this.DB
//                   , i = this.DB - o
//                   , s = (1 << o) - 1;
//                 r[0] = this[e] >> o;
//                 for (var n = e + 1; n < this.t; ++n)
//                     r[n - e - 1] |= (this[n] & s) << i,
//                     r[n - e] = this[n] >> o;
//                 o > 0 && (r[this.t - e - 1] |= (this.s & s) << i),
//                 r.t = this.t - e,
//                 r.clamp()
//             }
//         }
//         ,
//         i.prototype.subTo = function(t, r) {
//             for (var e = 0, o = 0, i = Math.min(t.t, this.t); e < i; )
//                 o += this[e] - t[e],
//                 r[e++] = o & this.DM,
//                 o >>= this.DB;
//             if (t.t < this.t) {
//                 for (o -= t.s; e < this.t; )
//                     o += this[e],
//                     r[e++] = o & this.DM,
//                     o >>= this.DB;
//                 o += this.s
//             } else {
//                 for (o += this.s; e < t.t; )
//                     o -= t[e],
//                     r[e++] = o & this.DM,
//                     o >>= this.DB;
//                 o -= t.s
//             }
//             r.s = o < 0 ? -1 : 0,
//             o < -1 ? r[e++] = this.DV + o : o > 0 && (r[e++] = o),
//             r.t = e,
//             r.clamp()
//         }
//         ,
//         i.prototype.multiplyTo = function(t, r) {
//             var e = this.abs()
//               , o = t.abs()
//               , s = e.t;
//             for (r.t = s + o.t; --s >= 0; )
//                 r[s] = 0;
//             for (s = 0; s < o.t; ++s)
//                 r[s + e.t] = e.am(0, o[s], r, s, 0, e.t);
//             r.s = 0,
//             r.clamp(),
//             this.s != t.s && i.ZERO.subTo(r, r)
//         }
//         ,
//         i.prototype.squareTo = function(t) {
//             for (var r = this.abs(), e = t.t = 2 * r.t; --e >= 0; )
//                 t[e] = 0;
//             for (e = 0; e < r.t - 1; ++e) {
//                 var o = r.am(e, r[e], t, 2 * e, 0, 1);
//                 (t[e + r.t] += r.am(e + 1, 2 * r[e], t, 2 * e + 1, o, r.t - e - 1)) >= r.DV && (t[e + r.t] -= r.DV,
//                 t[e + r.t + 1] = 1)
//             }
//             t.t > 0 && (t[t.t - 1] += r.am(e, r[e], t, 2 * e, 0, 1)),
//             t.s = 0,
//             t.clamp()
//         }
//         ,
//         i.prototype.divRemTo = function(t, r, e) {
//             var o = t.abs();
//             if (!(o.t <= 0)) {
//                 var n = this.abs();
//                 if (n.t < o.t)
//                     return null != r && r.fromInt(0),
//                     void (null != e && this.copyTo(e));
//                 null == e && (e = s());
//                 var h = s()
//                   , c = this.s
//                   , a = t.s
//                   , u = this.DB - l(o[o.t - 1]);
//                 u > 0 ? (o.lShiftTo(u, h),
//                 n.lShiftTo(u, e)) : (o.copyTo(h),
//                 n.copyTo(e));
//                 var f = h.t
//                   , p = h[f - 1];
//                 if (0 != p) {
//                     var b = p * (1 << this.F1) + (f > 1 ? h[f - 2] >> this.F2 : 0)
//                       , m = this.FV / b
//                       , d = (1 << this.F1) / b
//                       , T = 1 << this.F2
//                       , v = e.t
//                       , y = v - f
//                       , g = null == r ? s() : r;
//                     for (h.dlShiftTo(y, g),
//                     e.compareTo(g) >= 0 && (e[e.t++] = 1,
//                     e.subTo(g, e)),
//                     i.ONE.dlShiftTo(f, g),
//                     g.subTo(h, h); h.t < f; )
//                         h[h.t++] = 0;
//                     for (; --y >= 0; ) {
//                         var _ = e[--v] == p ? this.DM : Math.floor(e[v] * m + (e[v - 1] + T) * d);
//                         if ((e[v] += h.am(0, _, e, y, 0, f)) < _)
//                             for (h.dlShiftTo(y, g),
//                             e.subTo(g, e); e[v] < --_; )
//                                 e.subTo(g, e)
//                     }
//                     null != r && (e.drShiftTo(f, r),
//                     c != a && i.ZERO.subTo(r, r)),
//                     e.t = f,
//                     e.clamp(),
//                     u > 0 && e.rShiftTo(u, e),
//                     c < 0 && i.ZERO.subTo(e, e)
//                 }
//             }
//         }
//         ,
//         i.prototype.invDigit = function() {
//             if (this.t < 1)
//                 return 0;
//             var t = this[0];
//             if (0 == (1 & t))
//                 return 0;
//             var r = 3 & t;
//             return (r = (r = (r = (r = r * (2 - (15 & t) * r) & 15) * (2 - (255 & t) * r) & 255) * (2 - ((65535 & t) * r & 65535)) & 65535) * (2 - t * r % this.DV) % this.DV) > 0 ? this.DV - r : -r
//         }
//         ,
//         i.prototype.isEven = function() {
//             return 0 == (this.t > 0 ? 1 & this[0] : this.s)
//         }
//         ,
//         i.prototype.exp = function(t, r) {
//             if (t > 4294967295 || t < 1)
//                 return i.ONE;
//             var e = s()
//               , o = s()
//               , n = r.convert(this)
//               , h = l(t) - 1;
//             for (n.copyTo(e); --h >= 0; )
//                 if (r.sqrTo(e, o),
//                 (t & 1 << h) > 0)
//                     r.mulTo(o, n, e);
//                 else {
//                     var c = e;
//                     e = o,
//                     o = c
//                 }
//             return r.revert(e)
//         }
//         ,
//         i.prototype.toString = function(t) {
//             if (this.s < 0)
//                 return "-" + this.negate().toString(t);
//             var r;
//             if (16 == t)
//                 r = 4;
//             else if (8 == t)
//                 r = 3;
//             else if (2 == t)
//                 r = 1;
//             else if (32 == t)
//                 r = 5;
//             else {
//                 if (4 != t)
//                     return this.toRadix(t);
//                 r = 2
//             }
//             var e, o = (1 << r) - 1, i = !1, s = "", n = this.t, h = this.DB - n * this.DB % r;
//             if (n-- > 0)
//                 for (h < this.DB && (e = this[n] >> h) > 0 && (i = !0,
//                 s = a(e)); n >= 0; )
//                     h < r ? (e = (this[n] & (1 << h) - 1) << r - h,
//                     e |= this[--n] >> (h += this.DB - r)) : (e = this[n] >> (h -= r) & o,
//                     h <= 0 && (h += this.DB,
//                     --n)),
//                     e > 0 && (i = !0),
//                     i && (s += a(e));
//             return i ? s : "0"
//         }
//         ,
//         i.prototype.negate = function() {
//             var t = s();
//             return i.ZERO.subTo(this, t),
//             t
//         }
//         ,
//         i.prototype.abs = function() {
//             return this.s < 0 ? this.negate() : this
//         }
//         ,
//         i.prototype.compareTo = function(t) {
//             var r = this.s - t.s;
//             if (0 != r)
//                 return r;
//             var e = this.t;
//             if (0 != (r = e - t.t))
//                 return r;
//             for (; --e >= 0; )
//                 if (0 != (r = this[e] - t[e]))
//                     return r;
//             return 0
//         }
//         ,
//         i.prototype.bitLength = function() {
//             return this.t <= 0 ? 0 : this.DB * (this.t - 1) + l(this[this.t - 1] ^ this.s & this.DM)
//         }
//         ,
//         i.prototype.mod = function(t) {
//             var r = s();
//             return this.abs().divRemTo(t, null, r),
//             this.s < 0 && r.compareTo(i.ZERO) > 0 && t.subTo(r, r),
//             r
//         }
//         ,
//         i.prototype.modPowInt = function(t, r) {
//             var e;
//             return e = t < 256 || r.isEven() ? new p(r) : new b(r),
//             this.exp(t, e)
//         }
//
// function i(t, r, e) {
//             null != t && ("number" == typeof t ? this.fromNumber(t, r, e) : null == r && "string" != typeof t ? this.fromString(t, 256) : this.fromString(t, r))
//         }
//
//        var E=i
//
// var w = function(t, r) {
//             this.modulus = new E(t,16),
//             this.encryptionExponent = new E(r,16)
//         }
//
//  const n = {
//             getPublicKey: function(t, r) {
//                 return new w(t,r)
//             },
//             encrypt: function(t, r) {
//                 return !!r && (!!(t = this.pkcs1pad2(t, r.modulus.bitLength() + 7 >> 3)) && (!!(t = t.modPowInt(r.encryptionExponent, r.modulus)) && (1 == (1 & (t = t.toString(16)).length) && (t = "0" + t),
//                 L.encode(B.decode(t)))))
//             },
//             pkcs1pad2: function(t, r) {
//                 if (r < t.length + 11)
//                     return null;
//                 for (var e = [], o = t.length - 1; o >= 0 && r > 0; )
//                     e[--r] = t.charCodeAt(o--);
//                 for (e[--r] = 0; r > 2; )
//                     e[--r] = Math.floor(254 * Math.random()) + 1;
//                 return e[--r] = 2,
//                 e[--r] = 0,
//                 new E(e)
//             }
//         }
//
//
// var r={
//     publickey_exp: "010001",
//     publickey_mod: "cbb2b4f5cb47ccaea1661cb8ce42aab26762d5e3b1e9a3b8fd9e57ae7de30c01062f7d83a9b17b81ce377f54011e2390cd21934c085604261905eeb2d619b972f331d1c616b8a7fd01529cc66d7ef7ae52a9b71597b75881409854d91ed9c986a9a83fd63a72a8f9b63179d340e2c8cb75cfe25d44381cabcec6c7ec019d226d5b9843e6ec99a201e62259488d9c541b401ebe417f9c9e3b8401fcbf3c1ffba9b4b5a4c316a9d090d94e6193f3ad1ad101bb120358f1e00b6ee76d1f54afb2888b51535f7d18038a4eacb036fc89c8d48dc744fe2d60282f183e0d753750066ba9ece3d64b749bed23923fed6a93f5b81d0c34a96bf3c778d731bdc45b987bf3",
//     timestamp: "1083928450000"
// }
//
// function f(t, r) {
//             let e = n.getPublicKey(r.publickey_mod, r.publickey_exp)
//               , o = n.encrypt(t, e);
//             return o
//         }
//
// console.log(f("thyqwert1",r))



RSA=require("rsa-javascript")
RSA.setMaxDigits(130)
key = new RSA.RSAKeyPair("10001","","c5f3a8ba15b73bdadb80992a12f29163386c26ba58fce9ab6d7d9198ff368b1ba7b006451a30bb3b45dab536632a5cc013b46876524296293db2a50e454db8fccc367b9234420401719e658026d71c66d9396d74f18fb7d7fea36f871a55443da0639bf130f2df37c9c94bf0d79038942f162d8fa45355b9c7af52e40b4c81fc24840f397855d07b4f66030377a7f71a6a94e4b44f9df1f3bd58ad0681588737784c236694bf154b112ae367d9c4f78c2c8485d59cfd9990c765a09f07abe05da7a34c997b45dce90fd8b4aa313b3c965e7e6bb5b30398e0b05bded62c6dea31c0af3e9fbb5a03c6c8587719186156fd76a11bc3c98fc6774b8c98b3553790f7"
)
result=RSA.encryptedString(key, 'thyqwert1')

console.log(result)