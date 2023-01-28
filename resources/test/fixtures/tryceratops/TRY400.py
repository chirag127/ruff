"""
Violation:
Use '.exception' over '.error' inside except blocks
"""

import logging

logger = logging.getLogger(__name__)


def bad():
    try:
        a = 1
    except Exception:
        logging.error("Context message here")

        logging.error("Context message here")


def bad():
    try:
        a = 1
    except Exception:
        logger.error("Context message here")

        logger.error("Context message here")


def bad():
    try:
        a = 1
    except Exception:
        log.error("Context message here")

        log.error("Context message here")


def bad():
    try:
        a = 1
    except Exception:
        self.logger.error("Context message here")

        self.logger.error("Context message here")


def good():
    try:
        a = 1
    except Exception:
        logger.exception("Context message here")


def good():
    try:
        a = 1
    except Exception:
        foo.exception("Context message here")
