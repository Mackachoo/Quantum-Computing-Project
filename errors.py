#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Custom error module
"""


class Error(Exception):
    """Base class for exceptions in this module.

    Parameters
    ----------
    expression : str
        Built-in error trace.

    Attributes
    ----------
    expression : str
        Built-in error trace
    """

    pass

class InputError(Error):
    """Exception raised for errors in the input.

    Parameters
    ----------
    expression : str
        Built-in error trace.

    Attributes
    ----------
    expression : str
        Built-in error trace
    message : str
        Custom explanation of the error
    """

    def __init__(self, expression):
        self.expression = expression
        self.message = "Input is not in valid format"

class MatrixError(Error):
    """Exception raised for unexpected errors in matrix representation used.

    Parameters
    ----------
    expression : str
        Built-in error trace.

    Attributes
    ----------
    expression : str
        Built-in error trace
    message : str
        Custom explanation of the error
    """

    def __init__(self, expression):
        self.expression = expression
        self.message = "Matrix is not as expected"
