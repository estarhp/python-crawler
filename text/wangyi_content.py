import requests

import json

from b64 import b64encode

from Crypto.Cipher import AES




headers={
                'referer': 'https://music.163.com/song?id=1899047747',
                'cookie': '_ntes_nnid=c31e79afa2c69f5b1dcfe05235d1d992,1662779353869; _ntes_nuid=c31e79afa2c69f5b1dcfe05235d1d992; NMTID=00OKZES5MVaA5KaDE-iukQCRvOdQjEAAAGDJV9j1Q; WEVNSM=1.0.0; WNMCID=bvzalm.1662779354055.01.0; WM_TID=UDZ7ynbwcidAEFBVAQLBT0xmM%2Bo4N8R%2B; __snaker__id=X0MPWS3Aj5dME0VB; gdxidpyhxdE=c8p8%2F2Thb%2BLDOqNvRE2RXYaKcHWtGVijoBf%2Bi9IUJNCY1y%5CRpUZYdaVA55Pnt6jRmjUspCfqr9ca5XvXjO8yy5oAj0gl4SKA9yEkTYyaJmOABgf%2BTVA3K6arEz4cobQgGxtPgfdauSypCTBsQHwZ4piu2jnsAsHcGoAxM786s%2F0QDLyi%3A1662780801434; _9755xjdesxxd_=32; YD00000558929251%3AWM_NI=Do4M5cZPAq6%2BuDVNluh0Dxj%2FsHFBN7OL8JJjgJus5HnBnYkTAsmgO%2BVcf%2F6oqZiP21s7sgRntT1jUg9EDIWXSKob%2FDzBtaxlxcQnVR7oWXcuMz9BNBMqI6q3rTEak4gxRkY%3D; YD00000558929251%3AWM_NIKE=9ca17ae2e6ffcda170e2e6ee95ca4dedbdfb99c6599bac8eb3c55a828b9e86d144f3a8a2b0cb7aa6ae81a6b22af0fea7c3b92a88b1fcaeb8699a908f92b521b79c9aafef7facf08c99e925b1988aa3cd3d8d94f8abc962a596bb94b844ae9ea2baea6083ada388ce2196bdaad0b565b386a7b1b13bb1e9bd88d166b88cff8bd86dfb9b8caad6549195a183ae50ba9ebc82fb68bcbd9f8fd55af5b199b9e27f8fa6f7a3cd4a8faf87d7f439b28c8b82ea40a5a89e8cdc37e2a3; YD00000558929251%3AWM_TID=lxiypklf5zNEBRUVAQfESw0mbW6L%2FLVm; _iuqxldmzr_=32; JSESSIONID-WYYY=X7RpyucrfO3hwWjqt3cQym0l5hJHzOFgWGDnhqeX0shUaemnUJMXSRobZVuorirCw6yxSwQrX%2BieJ1H%2BTemGEDtv%2F5hQ5FhiX%5C9z%5Ce%5ClbUGD%2BVQsRPrRcUb%2F%2BirUZ%2FSn%2BSvxKmeuy35pFfmnuuddvhhINJp%2BKbKg7j2lm%5CCkxb0YkrcU%3A1668411073430; WM_NI=DKj%2FXdjfK8dW0KJEKbbE5hfONrovuDJFIRV%2FQCIA3brGZQLMD%2BYLTXMyOfZV0j50j7JWF1g78bZwzFFOooTWAkUxkJHFTTCyP09DpDMrf%2FYXKnOznWhd9TL7WBj9Uqo%2FRVA%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6ee82ee3e969bbcd4c433aa8a8aa7c45e869e8f86d5469ce8a892eb438fb39e95f32af0fea7c3b92a8895a6d0db70aaba85d9e75df49586a6ca6aa29bfb89e5458eaea197f8508a9a87b3d525939d87a2b26ab29996b2cf4788f597add7548fa78187d95ef4b6fbd1e93d8a898ad2e63dfcbe9698f94e8691a190d75d83b59b99ea428c9a9cb5c27394f0f7a5f3508faeaad0dc5489b2819bed5dacbcf7b5cf3d959ea6dad87badf19eb7c437e2a3; playerid=23535412',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
        }


''' function a(a) {
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
        return setMaxDigits(131),
        d = new RSAKeyPair(b,"",c),
        e = encryptedString(d, a)
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
    window.asrsea = d,
    window.ecnonasr = e
}'''

i="UQyTEVbobyPdnlL1"
data={
    "rid": "R_SO_4_1899047747",
    "threadId": "R_SO_4_1899047747",
    "pageNo": "1",
    "pageSize": "20",
    "cursor": "-1",
    "offset": "0",
    "orderType": "1",
    "csrf_token": ""
}
g="0CoJUm6Qyw8W8jud"


def to_16(data):
    pad=16-len(data)%16
    data+=chr(pad) * pad
    return data

def encode(data,key):

    data=to_16(data)

    iv="0102030405060708"
    key=key
    aes=AES.new(IV=iv.encode('utf-8'),mode=AES.MODE_CBC,key=key.encode('utf-8'))
    bytes=aes.encrypt(data.encode('utf-8'))
    return str(b64encode(bytes),'utf-8')









def getenctetx(data) :
    first=encode(data,key=g)
    enctetx=encode(first,key=i)
    return enctetx




def getencSecKey():
    i='NlBDjbownb0uxtIA'
    return "9a5e916a3a23ea6e5c2050ead641328634dc669d69ceed57522a9c0c7c4b3278bfaeb6faa18aa0573b5468801b33003f7b34896013277894aa1ab6ac6354ccc5bc5ab89fbc7698a82bc1af3577baeeabfc78d20065bef4d38c6387acc4e14fcf123f4ec9cb353b2318ca64d7bfb57f2e62e0961e6d69c679680b4fa24a3083bb"


# JSON.stringify(i3x)='{"rid":"R_SO_4_1899047747","threadId":"R_SO_4_1899047747","pageNo":"1","pageSize":"20","cursor":"-1","offset":"0","orderType":"1","csrf_token":""}'
# buU3x(["流泪", "强"])='010001'
# '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
# buU3x(["爱心", "女孩", "惊恐", "大笑"])='0CoJUm6Qyw8W8jud'

if __name__ == '__main__':
        url = "https://music.163.com/weapi/comment/resource/comments/get"
        resp=requests.post(url,data={
            'params':getenctetx(json.dumps(data)),
            'encSecKey':getencSecKey()
        })
        print({
            'params':getenctetx(json.dumps(data)),
            'encSecKey':getencSecKey()})
        print(resp.text)









