"""Check that the constants are on the right side of the comparisons"""

# pylint: disable=singleton-comparison, missing-docstring, too-few-public-methods
# pylint: disable=comparison-of-constants

class MyClass:
    def __init__(self):
        self.attr = 1

    def dummy_return(self):
        return self.attr

def dummy_return():
    return 2

def bad_comparisons():
    """this is not ok"""
    instance = MyClass()
    for _ in range(10):
        if dummy_return() > 3:  # [misplaced-comparison-constant]
            pass
        if instance.dummy_return() != 4:  # [misplaced-comparison-constant]
            pass

def good_comparison():
    """this is ok"""

def double_comparison():
    """Check that we return early for non-binary comparison"""
    for i in range(10):
        if 2 <= i <= 8:
            print("Between 2 and 8 inclusive")

def const_comparison():
    """Check that we return early for comparison of two constants"""
