



t= 1671847429851
e= "fsdsogkndfokasodnaso"

const crypto = require("crypto")


var n='Z21kD9ZK1ke6ugku2ccWuz4Ip5f4PLCoxWstZf_6UUxIH0L_wO3JsbEy28GRk_H-JC_x_v9hx9EBZTV_ND9-PwcjHKevepty8KwjwTqrMQAVulkYf9Cv71_154x5WrU_Hc7GcAjXgfYypcrJF6P3aQeBUWVGm2pRZEN2ZTvAy4UKeA7P1A7-msfhYS3q6NJsRrObajdVmAyXqsnRtUimvqNIb7lUvBzf_Olcq-n0IPjem2vh40tuAWj20bW59Wj-X3Fl_YTVHiwj4J9BjU2TTcxxXXpn8K8wIdGvKzQWBQ0lW5OmhbFHtI5PbTbuO4r5'
var a='ydsecret://query/key/B*RGygVywfNBwpmBaZg*WT7SIOUP2T0C9WHMZN39j^DAdaZhAnxvGcCY6VYFwnHl'
var b='ydsecret://query/iv/C@lZe2YzHtZ2CYgaXKSVfsb7Y4QWHjITPPZ0nQp87fBeJ!Iv6v^6fvi2WN@bYpJ4'

function m(e){
    return crypto.createHash("md5").update(e).digest()
}

function A(t,o,n){

                const a = Buffer.alloc(16, m(o))
                  , r = Buffer.alloc(16, m(n))

                  , i = crypto.createDecipheriv("aes-128-cbc", a, r);
                let s = i.update(t, "base64", "utf-8");
                return s += i.final("utf-8"),
                s
            }









console.log(A(n,a,b))