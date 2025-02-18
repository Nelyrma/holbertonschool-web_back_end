#!/usr/bin/env python3
"""
filtered logger module
"""
import re


def filter_datum(fields, redaction, message, separator):
    """
    returns the log message obfuscated
    """

    # built a regex for fields
    pattern = r'(' + '|'.join(fields) + rf'){separator}[^{separator}]+'
    # replace the fields values with the redaction
    return re.sub(pattern, rf'\1{separator}{redaction}', message)
