#!/usr/bin/env python3
"""
filtered logger module
"""
import logging
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


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        filter values in incoming log records using filter_datum
        """
        record.msg = filter_datum(
            self.fields, self.REDACTION, record.msg, self.SEPARATOR
        )
        return super().format(record)
