def f():
    return any(check(x) for x in iterable)


def f():
    return next((True for x in iterable if check(x)), True)


def f():
    for el in [1, 2, 3]:
        if is_true(el):
            return True
    raise Exception


def f():
    return not any(check(x) for x in iterable)


def f():
    return all(x.is_empty() for x in iterable)


def f():
    return next((False for x in iterable if check(x)), False)


def f():
    return next(("foo" for x in iterable if check(x)), "bar")


def f():
    return any(check(x) for x in iterable)


def f():
    return not any(check(x) for x in iterable)


def f():
    return any(check(x) for x in iterable)


def f():
    return not any(check(x) for x in iterable)


def f():
    for x in iterable:
        if check(x):
            return True
        elif x.is_empty():
            return True
    return False


def f():
    for x in iterable:
        return True if check(x) else True
    return False


def f():
    for x in iterable:
        if check(x):
            return True
        elif x.is_empty():
            return True
    return True
