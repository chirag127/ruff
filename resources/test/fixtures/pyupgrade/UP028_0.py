def f():
    yield from y


def g():
    yield from z


def h():
    yield from [1, 2, 3]


def i():
    yield from set(y)


def j():
    yield from (1, 2, 3)


def k():
    yield from {3: "x", 6: "y"}


def f():  # Comment one\n'
    # Comment two\n'
    yield from {  # Comment three\n'
        3: "x",  # Comment four\n'
        # Comment five\n'
        6: "y",  # Comment six\n'
    }
        # Comment ten',


def f():
    yield from [{3: (3, [44, "long ss"]), 6: "y"}]


def f():
    yield from z()

def f():
    def func():
        # This comment is preserved\n'
        yield from z()
            # Comment four\n'
# Comment\n'
def g():
    print(3)


def f():
    yield from y
    yield from x


def f():
    yield from z()
    x = 1
