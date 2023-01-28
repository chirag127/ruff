def f() -> int:
    yield 1


class Foo:
    pass

await f()
