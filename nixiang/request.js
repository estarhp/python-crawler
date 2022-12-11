const crypto=require('crypto')


e={
    "ts": (new Date).getTime(),
    "pageNo": 3,
    "pageSize": 20,
    "total": 6559,
    "AREACODE": "",
    "M_PROJECT_TYPE": "",
    "KIND": "GCJS",
    "GGTYPE": "1",
    "PROTYPE": "",
    "timeType": "6",
    "BeginTime": "2022-05-25 00:00:00",
    "EndTime": "2022-11-25 23:59:59",
    "createTime": []
}

function u(t, e) {
            return t.toString().toUpperCase() > e.toString().toUpperCase() ? 1 : t.toString().toUpperCase() == e.toString().toUpperCase() ? 0 : -1
        }

function l(t) {
            for (var e = Object.keys(t).sort(u), n = "", a = 0; a < e.length; a++)
                if (void 0 !== t[e[a]])
                    if (t[e[a]] && t[e[a]]instanceof Object || t[e[a]]instanceof Array) {
                        var i = JSON.stringify(t[e[a]]);
                        n += e[a] + i
                    } else
                        n += e[a] + t[e[a]];
            return n
        }



s=function (e) {
    return crypto.createHash('md5').update(e).digest('hex')
}
function d(t) {
            for (var e in t)
                "" !== t[e] && void 0 !== t[e] || delete t[e];
            var n = '3637CB36B2E54A72A7002978D0506CDF' + l(t);
            return s(n).toLocaleLowerCase()
        }

console.log(d(e))



