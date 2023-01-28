class MyException(Exception):
    pass


def bad():
    try:
        a = process()
        raise MyException(a)

    except Exception:
        logger.exception("something failed")


def good():
    try:
        a = process()  # This throws the exception now
    except MyException:
        logger.exception("a failed")
    except Exception:
        logger.exception("something failed")
