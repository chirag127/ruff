from abc import ABCMeta

import pydantic


class Class:
    def bad_method(self):
        pass

    if False:

        def extra_bad_method(self):
            pass

    def good_method(self):
        pass

    @classmethod
    def class_method(cls):
        pass

    @staticmethod
    def static_method(x):
        return x

    @pydantic.validator
    def lower(cls, my_field: str) -> str:
        pass

    @pydantic.validator("my_field")
    def lower(cls, my_field: str) -> str:
        pass

    def __init__(self):
        ...

    def __new__(cls, *args, **kwargs):
        ...

    def __init_subclass__(cls, default_name, **kwargs):
        ...


class MetaClass(ABCMeta):
    def bad_method(self):
        pass

    def good_method(self):
        pass


def func(x):
    return x
