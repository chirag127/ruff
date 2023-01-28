# These should NOT change
def f():
    for _ in z:
        yield


def f():
    for _ in z:
        yield y


def f():
    for x, y in z:
        yield x


def f():
    for x, y in z:
        yield y


def f():
    for a, b in z:
        yield x, y


def f():
    for x, y in z:
        yield y, x


def f():
    for x, y, c in z:
        yield x, y


def f():
    for _ in z:
        yield 22


def f():
    yield from z
    print("boom!")


def f():
    yield from range(5)
    print(x)


def f():
    def g():
        print(x)

    yield from range(5)
    g()


def f():
    def g():
        def h():
            print(x)

        return h

    yield from range(5)
    g()()


def f(x):
    yield from y
    del x


async def f():
    for x in y:
        yield x


def f():
    x = 1
    print(x)
    yield from y


def f():
    yield from y
    print(x)


def f():
    yield from y
    z = lambda: x


def f():
    yield from y
    class C:
        def __init__(self):
            print(x)


def f():
    for x in y:
        yield x, x + 1


def f():
    for x, y in z:
        yield x, y, x + y
