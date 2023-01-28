"""
Violation:

Prefer TypeError when relevant.
"""


def incorrect_basic(some_arg):
    if not isinstance(some_arg, int):
        raise Exception("...")  # should be typeerror


def incorrect_multiple_type_check(some_arg):
    if not isinstance(some_arg, (int, str)):
        raise Exception("...")  # should be typeerror


class MyClass:
    pass


def incorrect_with_issubclass(some_arg):
    if not issubclass(some_arg, MyClass):
        raise Exception("...")  # should be typeerror


def incorrect_with_callable(some_arg):
    if not callable(some_arg):
        raise Exception("...")  # should be typeerror


def incorrect_ArithmeticError(some_arg):
    if not isinstance(some_arg, int):
        raise ArithmeticError("...")  # should be typeerror


def incorrect_AssertionError(some_arg):
    if not isinstance(some_arg, int):
        raise AssertionError("...")  # should be typeerror


def incorrect_AttributeError(some_arg):
    if not isinstance(some_arg, int):
        raise AttributeError("...")  # should be typeerror


def incorrect_BufferError(some_arg):
    if not isinstance(some_arg, int):
        raise BufferError  # should be typeerror


def incorrect_EOFError(some_arg):
    if not isinstance(some_arg, int):
        raise EOFError("...")  # should be typeerror


def incorrect_ImportError(some_arg):
    if not isinstance(some_arg, int):
        raise ImportError("...")  # should be typeerror


def incorrect_LookupError(some_arg):
    if not isinstance(some_arg, int):
        raise LookupError("...")  # should be typeerror


def incorrect_MemoryError(some_arg):
    if not isinstance(some_arg, int):
        # should be typeerror
        # not multiline is on purpose for fix
        raise MemoryError(
            "..."
        )


def incorrect_NameError(some_arg):
    if not isinstance(some_arg, int):
        raise NameError("...")  # should be typeerror


def incorrect_ReferenceError(some_arg):
    if not isinstance(some_arg, int):
        raise ReferenceError("...")  # should be typeerror


def incorrect_RuntimeError(some_arg):
    if not isinstance(some_arg, int):
        raise RuntimeError("...")  # should be typeerror


def incorrect_SyntaxError(some_arg):
    if not isinstance(some_arg, int):
        raise SyntaxError("...")  # should be typeerror


def incorrect_SystemError(some_arg):
    if not isinstance(some_arg, int):
        raise SystemError("...")  # should be typeerror


def incorrect_ValueError(some_arg):
    if not isinstance(some_arg, int):
        raise ValueError("...")  # should be typeerror


def incorrect_not_operator_isinstance(some_arg):
    if isinstance(some_arg):
        raise Exception("...")  # should be typeerror


def incorrect_and_operator_isinstance(arg1, arg2):
    if not isinstance(some_arg) or not isinstance(arg2):
        raise Exception("...")  # should be typeerror


def incorrect_or_operator_isinstance(arg1, arg2):
    if not isinstance(some_arg) and not isinstance(arg2):
        raise Exception("...")  # should be typeerror


def incorrect_multiple_operators_isinstance(arg1, arg2, arg3):
    if (isinstance(arg1) or not isinstance(arg2)) and not isinstance(arg3):
        raise Exception("...")  # should be typeerror


def incorrect_not_operator_callable(some_arg):
    if callable(some_arg):
        raise Exception("...")  # should be typeerror


def incorrect_and_operator_callable(arg1, arg2):
    if not callable(some_arg) or not callable(arg2):
        raise Exception("...")  # should be typeerror


def incorrect_or_operator_callable(arg1, arg2):
    if not callable(some_arg) and not callable(arg2):
        raise Exception("...")  # should be typeerror


def incorrect_multiple_operators_callable(arg1, arg2, arg3):
    if (callable(arg1) or not callable(arg2)) and not callable(arg3):
        raise Exception("...")  # should be typeerror


def incorrect_not_operator_issubclass(some_arg):
    if issubclass(some_arg):
        raise Exception("...")  # should be typeerror


def incorrect_and_operator_issubclass(arg1, arg2):
    if not issubclass(some_arg) or not issubclass(arg2):
        raise Exception("...")  # should be typeerror


def incorrect_or_operator_issubclass(arg1, arg2):
    if not issubclass(some_arg) and not issubclass(arg2):
        raise Exception("...")  # should be typeerror


def incorrect_multiple_operators_issubclass(arg1, arg2, arg3):
    if (issubclass(arg1) or not issubclass(arg2)) and not issubclass(arg3):
        raise Exception("...")  # should be typeerror


def incorrect_multi_conditional(arg1, arg2):
    if isinstance(arg1, int):
        pass
    elif isinstance(arg2, int):
        raise Exception("...")  # should be typeerror


class MyCustomTypeValidation(Exception):
    pass


def correct_custom_exception(some_arg):
    if not isinstance(some_arg, int):
        raise MyCustomTypeValidation("...")  # that's correct, because it's not vanilla


def correct_complex_conditional(val):
    if val is not None and (not isinstance(val, int) or val < 0):
        raise ValueError(...)  # fine if this is not a TypeError


def correct_multi_conditional(some_arg):
    if some_arg != 3 and not isinstance(some_arg, int):
        raise Exception("...")  # fine if this is not a TypeError


def correct_should_ignore(some_arg):
    if not isinstance(some_arg, int):
        raise TypeError("...")


def check_body(some_args):
    if isinstance(some_args, int):
        raise ValueError("...") # should be typeerror


def check_body_correct(some_args):
    if isinstance(some_args, int):
        raise TypeError("...") # correct


def multiple_elifs(some_args):
    if not isinstance(some_args, int) or some_args < 3 or some_args > 10:
        raise ValueError("...") # should be typerror


def multiple_ifs(some_args):
    if not isinstance(some_args, int):
        raise ValueError("...") # should be typerror
    if some_args >= 3 and some_args > 10 or some_args < 3:
        raise ValueError("...")  # this is ok if we don't simplify


def early_return():
    if isinstance(this, some_type):
        if x in this:
            return

        raise ValueError(f"{this} has a problem")  # this is ok


def early_break():
    for x in this:
        if isinstance(this, some_type):
            if x in this:
                break

            raise ValueError(f"{this} has a problem")  # this is ok


def early_continue():
    for x in this:
        if isinstance(this, some_type) and x not in this:
            raise ValueError(f"{this} has a problem")  # this is ok


def early_return_else():
    if not isinstance(this, some_type):
        if x in this:
            return

        raise ValueError(f"{this} has a problem")  # this is ok
