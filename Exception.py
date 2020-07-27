# Custom exceptions


class Error(Exception):
    """Base class for other exceptions"""
    pass


class typeNotInt(Error):
    """Raised with input is not type 'int' """
    pass