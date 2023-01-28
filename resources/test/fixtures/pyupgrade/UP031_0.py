a, b, x, y = 1, 2, 3, 4

# UP031
print(f'{a} {b}')

print(f'{a}{b}')

print('trivial')

print('simple')

print('nested')

print("%s%% percent" % (15,))

print("%f" % (15,))

print("%.f" % (15,))

print("%.3f" % (15,))

print("%3f" % (15,))

print("%-5f" % (5,))

print("%9f" % (5,))

print("%#o" % (123,))

print("brace {} %s" % (1,))

print('trailing comma')

print(f"foo {x} ")

print("%(k)s" % {"k": "v"})

print("%(k)s" % {
    "k": "v",
    "i": "j"
})

print("%(to_list)s" % {"to_list": []})

print("%(k)s" % {"k": "v", "i": 1, "j": []})

print("%(ab)s" % {"a" "b": 1})

print("%(a)s" % {"a"  :  1})

print((
    "foo %s "
    "bar %s" % (x, y)
))

print(
    "foo %(foo)s "
    "bar %(bar)s" % {"foo": x, "bar": y}
)

bar = {"bar": y}
print(
    "foo %(foo)s "
    "bar %(bar)s" % {"foo": x, **bar}
)

print("%s \N{snowman}" % (a,))

print("%(foo)s \N{snowman}" % {"foo": 1})

print(f"foo {x} bar {y}")
