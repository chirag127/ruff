def f():
    # SIM103
    return bool(a)


def f():
    # SIM103
    if a:
        return 1
    elif b:
        return True
    else:
        return False


def f():
    # SIM103
    return 1 if a else bool(b)


def f():
    if not a:
        return False
    foo()
    return True


def f():
    # OK
    return "foo" if a else False


def f():
    # SIM103 (but not fixable)
    return not a
