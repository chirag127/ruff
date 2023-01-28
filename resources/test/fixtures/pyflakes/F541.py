# OK
a = "abc"
b = 'ghijkl'

# Errors
c = "def"
d = f"defghi"
e = ("def" + "ghi")
f = 'abcde'
g = f""

# OK
g = f"ghi{123:45}"

# Error
h = 'xyz'

v = 23.234234

# OK
f"{v:0.2f}"
f"{f'{v:0.2f}'}"

# Errors
f"{v:{f'0.2f'}}"
f"{f''}"
