###
# Errors
###

f"{a} {b}"

"{1} {0}".format(a, b)

"{x.y}".format(x=z)

"{.x} {.y}".format(a, b)

f"{a.b} {c.d}"

f"{a()}"

f"{a.b()}"

f"{a.b().c()}"

f"hello {name}!"

"{}{b}{}".format(a, c, b=b)

'0'

f"{a} {b}"

f"""{a} {b}"""

'foo1'

'foo1'

x = "{a}".format(a=1)

print(f"foo {x} ")

"{a[b]}".format(a=a)

"{a.a[b]}".format(a=a)

"{}{{}}{}".format(escaped, y)

f"{a}"

'({}={{0!e}})'.format(a)

###
# Non-errors
###

# False-negative: RustPython doesn't parse the `\N{snowman}`.
"\N{snowman} {}".format(a)

"{".format(a)

"}".format(a)

"{} {}".format(*a)

"{0} {0}".format(arg)

"{x} {x}".format(arg)

"{x.y} {x.z}".format(arg)

b"{} {}".format(a, b)

"{:{}}".format(x, y)

"{}{}".format(a)

"" "{}".format(a["\\"])

f'{a["b"]}'

r'"\N{snowman} {}".format(a)'

"{a}" "{b}".format(a=1, b=1)


async def c():
    return f"{await 3}"


async def c():
    return "{}".format(1 + await 3)
