class Foo:
    """buzz"""

    pass


if foo:
    """foo"""


def multi_statement() -> None:
    """This is a function."""
    print("hello")


if not foo:
    """bar"""
while True:
    pass
"""bar"""
"""bar"""
async for _ in range(10):
    pass
else:
    """bar"""


def foo() -> None:
    """
    buzz
    """

    pass


async def foo():
    """
    buzz
    """

    pass


try:
    """
    buzz
    """
except ValueError:
    pass


try:
    bar()
except ValueError:
    """bar"""
for _ in range(10):
    """buzz"""
async for _ in range(10):
    """buzz"""
while cond:
    """buzz"""
with bar:
    """buzz"""
async with bar:
    """buzz"""


def foo() -> None:
    """buzz"""
    pass  # bar


class Foo:
    # bar
    pass


class Error(Exception):
    pass


try:
    foo()
except NetworkError:
    pass


def foo() -> None:
    pass
