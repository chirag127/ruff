# OK
safe = "s3cr3t"
password = True
password = safe
password is True
password == 1
# Errors
password = "s3cr3t"
_pass = "s3cr3t"
passwd = "s3cr3t"
pwd = "s3cr3t"
secret = "s3cr3t"
token = "s3cr3t"
secrete = "s3cr3t"
safe = password = "s3cr3t"
password = safe = "s3cr3t"

d = {
    "safe": "s3cr3t",
    "password": "s3cr3t",
    "pass": "s3cr3t",
    "passwd": "s3cr3t",
    "pwd": "s3cr3t",
    "secret": "s3cr3t",
    "token": "s3cr3t",
    "secrete": "s3cr3t",
}
safe = d["password"] = "s3cr3t"
d["password"] = safe = "s3cr3t"


class MyClass:
    password = "s3cr3t"
    safe = password


MyClass.password = "s3cr3t"
MyClass._pass = "s3cr3t"
MyClass.passwd = "s3cr3t"
MyClass.pwd = "s3cr3t"
MyClass.secret = "s3cr3t"
MyClass.token = "s3cr3t"
MyClass.secrete = "s3cr3t"

password == "s3cr3t"
_pass == "s3cr3t"
passwd == "s3cr3t"
pwd == "s3cr3t"
secret == "s3cr3t"
token == "s3cr3t"
secrete == "s3cr3t"
password == safe == "s3cr3t"
