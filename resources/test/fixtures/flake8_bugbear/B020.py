"""
Should emit:
B020 - on lines 8, 21, and 36
"""


items = [1, 2, 3]

for items in items:
    print(items)

items = [1, 2, 3]

for item in items:
    print(item)

values = {"secret": 123}

for key, value in values.items():
    print(f"{key}, {value}")

for key, values in values.items():
    print(f"{key}, {values}")

# Variables defined in a comprehension are local in scope
# to that comprehension and are therefore allowed.
for var in list(range(10)):
    print(var)

for var in iter(range(10)):
    print(var)

for k, v in dict(zip(range(10), range(10, 20))).items():
    print(k, v)

# However we still call out reassigning the iterable in the comprehension.
for vars in list(vars):
    print(vars)

for var in sorted(range(10), key=lambda var: var.real):
    print(var)
