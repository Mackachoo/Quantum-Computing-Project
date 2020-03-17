#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Error module
    TODO: Add all custom errors (input, matrix multiplication diff shapes...)
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
        TODO: Custom explanation of the error
    """

    def __init__(self, expression):
        self.expression = expression
        self.message = ""
