###
# Positive cases
###

# SIM401 (pattern-1)
var = a_dict[key] if key in a_dict else "default1"
# SIM401 (pattern-2)
var = "default2" if key not in a_dict else a_dict[key]
# SIM401 (default with a complex expression)
var = a_dict[key] if key in a_dict else val1 + val2
# SIM401 (complex expression in key)
var = a_dict[keys[idx]] if keys[idx] in a_dict else "default"
# SIM401 (complex expression in dict)
var = dicts[idx][key] if key in dicts[idx] else "default"
# SIM401 (complex expression in var)
vars[idx] = a_dict[key] if key in a_dict else "default"
###
# Negative cases
###

# OK (false negative)
var = "default" if key not in a_dict else a_dict[key]
# OK (different dict)
var = other_dict[key] if key in a_dict else "default"
var2 = value2
if key in a_dict:
    var = a_dict[other_key]
    var = a_dict[key]
    var = a_dict[key]
    var = a_dict[key]
    var = a_dict[key]
else:
    var = "default"

    other_var = "default"

    var = "default"

    var = "default"

    var = foo()

# OK (complex default value)
var = a_dict[key] if key in a_dict else a_dict["fallback"]
# OK (false negative for elif)
if foo():
    pass
elif key in a_dict:
    vars[idx] = a_dict[key]
else:
    vars[idx] = "default"

# OK (false negative for nested else)
if not foo():
    vars[idx] = a_dict[key] if key in a_dict else "default"
