dog = {"bob": "bob"}

# Single placeholder always fine
f"{dog}"
"%s" % {"bob": "bob"}
"%s" % {**{"bob": "bob"}}
f'{["bob"]}'
'bob'
f'{{"bob"}}'
f'{[*["bob"]]}'
f'{{"bob": "bob" for _ in range(1)}}'
f'{["bob" for _ in range(1)]}'
f'{("bob" for _ in range(1))}'
f'{{"bob" for _ in range(1)}}'
# Multiple placeholders
"%s %s" % dog
"%s %s" % {"bob": "bob"}  # F503
"%s %s" % {**{"bob": "bob"}}  # F503
"%s %s" % ["bob"]
"%s %s" % ("bob",)
"%s %s" % {"bob"}
"%s %s" % [*["bob"]]
"%s %s" % {"bob": "bob" for _ in range(1)}  # F503
"%s %s" % ["bob" for _ in range(1)]
"%s %s" % ("bob" for _ in range(1))
"%s %s" % {"bob" for _ in range(1)}
