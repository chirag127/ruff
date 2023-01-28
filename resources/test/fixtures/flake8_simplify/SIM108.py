# SIM108
b = c if a else d
# OK
b = c if a else d

# OK
if a:
    b = c
elif c:
    b = a
else:
    b = d

import sys

# OK
if sys.version_info >= (3, 9):
    randbytes = random.randbytes
else:
    randbytes = _get_random_bytes

# OK
randbytes = random.randbytes if sys.platform == "darwin" else _get_random_bytes
# OK
if sys.platform.startswith("linux"):
    randbytes = random.randbytes
else:
    randbytes = _get_random_bytes


# OK (includes comments)
abc = x if x > 0 else -x
# OK (too long)
if parser.errno == BAD_FIRST_LINE:
    req = wrappers.Request(sock, server=self._server)
else:
    req = wrappers.Request(
        sock,
        parser.get_method(),
        parser.get_scheme() or _scheme,
        parser.get_path(),
        parser.get_version(),
        parser.get_query_string(),
        server=self._server,
    )


# SIM108
if a:
    b = cccccccccccccccccccccccccccccccccccc
else:
    b = ddddddddddddddddddddddddddddddddddddd


if a:
    b = cccccccccccccccccccccccccccccccccccc
else:
    b = ddddddddddddddddddddddddddddddddddddd
