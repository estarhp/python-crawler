
const RSA =require("rsa-js-java/RSA")

var rsa = function (arg) {
      RSA.setMaxDigits(130)
      var modulus = "be44aec4d73408f6b60e6fe9e3dc55d0e1dc53a1e171e071b547e2e8e0b7da01c56e8c9bcf0521568eb111adccef4e40124b76e33e7ad75607c227af8f8e0b759c30ef283be8ab17a84b19a051df5f94c07e6e7be5f77866376322aac944f45f3ab532bb6efc70c1efa524d821d16cafb580c5a901f0defddea3692a4e68e6cd";
      var key = new RSA.RSAKeyPair("10001","",modulus)
      return RSA.encryptedString(key, arg)}




console.log(rsa('thyqwert'))