#!/usr/bin/env python3
"""
filtered logger module
"""
import re
from typing import List, Tuple


def filter_datum(
    fields: List[str],
    redaction: str,
    message: str,
    separator: str
) -> str:
    """
    returns the log message obfuscated
    """
    for field in fields:
        # built a regex for fields
        pattern = r"(?<={}=)[^{}]+(?={})".format(field, separator, separator)
        # replace the fields values with the redaction
        message = re.sub(pattern, redaction, message)
    return message
