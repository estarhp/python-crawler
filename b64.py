import base64

n="aHR0cHM6Ly9lcGF5LjE2My5jb20vaDVDYXNoaWVyL2JlZm9yZS12YWxpZGF0aW9u"
n=base64.b64decode(n)

print(n.decode())