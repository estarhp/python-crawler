const js=require('crypto-js')
function b(t) {
    var e = js.enc.Utf8.parse('BE45D593014E4A4EB4449737660876CE')
        , n = js.enc.Utf8.parse('A8909931867B0425')
        , a = js.AES.decrypt(t, e, {
        iv: n,
        mode: js.mode.CBC,
        padding: js.pad.Pkcs7
    });
    return a.toString(js.enc.Utf8)
}
data="MgwXi0KD1jGM575jK3LON58XYQrUR1goy7Unh54JnehzDbDxCXw6piS+aU5c2ocHtQjAN1kXgyHFs2YA3IdDRO2eqznJFVQeokMzj3AT2BQyWT8AO50ASbdIjodPf28rBnIkz+tny7JSoIYDUxZjmBz9S+dJOmo2QzHowt8SZuZOFF81SMbmje5ev1nLnBpG/N8eNBB5lYiJKlyMXVGNQ3nmXce1q2+X/9sfKXlWiQYIRUIKoFys8VjvGw4DWAelTNAqoxkxCyC/nLNs+CrxGBf5baFUfMzXGFzROeoPIsnKyU+4lA86MGvJiHe+vNFwU3gUbPt1Bct9ncqkP3nXhv7Gd5DS1FPhoyczCpRcMYVQsDWR3og8ZltfetZITTJY1lBOFq4+o9Ua8bNZmcTkAe5GgpILtVyvDIV/s3xBX1bfto9Qbuv6uuLOIUC0Lje3GKfA8VRp2YzQSECtDiGmRtCLZQRYeH8XWKG+PNg1inBLn6m6owzG8c+wXlHr3VdmYTWmDAQPCuHTxKUtXI6b0WobIsv7Lto1VAULWXH31DIEogMmjaApRt3yGp2rVnkXVfGd94Za4n57tpmz8i/3hNUiVx9IHJ4sYy9XFk8OZaJs03aX5nFqLZPTz1YhyJOzNAQ9BCXmVDJOUcshQPRtx4id8llLPN+0Anl7cPXhpWbiz2bxqXxSqAPk2WwioaL40vsntwiYf3l6oMz6m08NQTYaAxOFFBRydROPHQ1L8xZ7dhAMuKwGuNHGeW1dB4lHMh9w/+oVhvGaBpaC5UzAzGYXdt1ebc7+UgFh+rWLFXL+39K6pD78EemiiYjAr/Vvai276jsJ+sfseZ1EzbSYP1vxG8YMwesyVX8m+Zjo+fX0Fvex9Ae9Rpken8jPO0clgK1p8wEORGsnWNIeLbKEKt34I++smRSfp0BtS2IwidpxobbbJzrH0Te4mXpdiYYDg8STRCEPgWmaiBriw1JV6I/FUMX8Jc8SEbOEVsV8Id+L0raEWHIdMlbcCKn9lzKJwwkfJUaOzZeVoJJ77X3Hb1Tz7O/lvDAkFjKP/1O6QvSCC7AdKyf7Qew0yTBwKBM6FSf09reNfMOjmmQh3C13+j9z6rVD6XboCscOhQvKhro2v9TO5CJCYaDjeovzzOBE9pgT7YxrDxgbWK0tjss0obOku6QgzV8jqdV781oDfK+KtCNV7RgfWG6+kF9ZO9ecZ5GcIxRSS22JkFjKsvmxnkW1bqZwzIO52BkgQMx/7Eod/LKIuqCmoc41w3wiobBnCEywDEtAmSUBeGdqqn9OPxfdPkz4BTn/qbmhrb001ZA9abvtSGmg9UXMkvZiYZbZRjWiETEeEFMxGdkSt1rEeTZSx/BoqgZ8ZHdqvnSZBmdbU8CaUYT0a3mP50tRnMDclQITKuVrzxE1UxpOm5TNHa3Xj+zjEs42GTIta8ykqG4gBGieDyqHYVtJI+XG/kcZzTEmpdcVVjHaZJKzssVjeOawl6UcYGC6fmggNb04kNZlTZdgyT2TwjPg4c+BpdGuHFDO+wr7cFZMJE//FiBrh05NeLcu7+VeA3BlYV2Mnws="
console.log(b(data))


