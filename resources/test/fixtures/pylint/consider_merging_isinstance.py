"""Checks use of consider-merging-isinstance"""
# pylint:disable=line-too-long, simplifiable-condition


def isinstances():
    "Examples of isinstances"
    var = range(10)

    result = isinstance(var[2], (int, float))

    result = isinstance(var[4], (int, float)) or isinstance(var[5], list) and False

    result = isinstance(var[5], int) or True or isinstance(var[5], float)  # [consider-merging-isinstance]

    inferred_isinstance = isinstance
    result = inferred_isinstance(var[6], int) or inferred_isinstance(var[6], float) or inferred_isinstance(var[6], list) and False   # [consider-merging-isinstance]
    result = isinstance(var[10], str) or isinstance(var[10], int) and var[8] * 14 or isinstance(var[10], float) and var[5] * 14.4 or isinstance(var[10], list)   # [consider-merging-isinstance]
    result = isinstance(var[11], (int, int, float))

    result = isinstance(var[20])
    result = isinstance()

    # Combination merged and not merged
    result = isinstance(var[12], (int, float, list))

    # not merged but valid
    result = isinstance(var[5], int) and var[5] * 14 or isinstance(var[5], float) and var[5] * 14.4
    result = isinstance(var[7], int) or not isinstance(var[7], float)
    result = isinstance(var[6], int) or isinstance(var[7], float)
    result = isinstance(var[6], int) or isinstance(var[7], int)
    return isinstance(var[6], (float, int)) or False
