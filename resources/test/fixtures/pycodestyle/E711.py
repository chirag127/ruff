#: E711
if TrueElement.get_element(True) == TrueElement.get_element(False):
    pass

assert (not foo) in bar
assert {"x": not foo} in bar
assert [42, not foo] in bar
