#: E721
#: E721
import types

#: E721
import types

#: E721
assert type(res) == type(False)
#: E721
assert type(res) == type([])
#: E721
assert type(res) == type(())
#: E721
assert type(res) == type((0,))
#: E721
assert type(res) == type((0))
#: E721
assert type(res) != type((1,))
#: E721
assert type(res) is type((1,))
#: E721
assert type(res) is not type((1,))
#: E211 E721
assert type(res) == type(
    [
        2,
    ]
)
#: E201 E201 E202 E721
assert type(res) == type(())
#: E201 E202 E721
assert type(res) == type((0,))

#: Okay
import types

assert type(res) == type(None)
