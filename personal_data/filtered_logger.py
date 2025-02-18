#!/usr/bin/env python3
"""
filtered logger module
"""
import logging
import mysql.connector
import os
import re
from typing import List, Tuple


PII_FIELDS: Tuple = ("name", "email", "phone", "ssn", "password")


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


def get_logger() -> logging.Logger:
    """
    create a logger that uses RedactingFormatter"""

    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    # create a StreamHandler
    stream_handler = logging.StreamHandler()

    # using RedactingFormatter to format logs
    formatter = RedactingFormatter(fields=PII_FIELDS)
    stream_handler.setFormatter(formatter)

    # add the handler to the log
    logger.addHandler(stream_handler)

    return logger


def get_db() -> mysql.connector.MySQLConnection:
    """
    returns a connector to the database
    """
    db_username = os.getenv('PERSONAL_DATA_DB_USERNAME', 'root')
    db_password = os.getenv('PERSONAL_DATA_DB_PASSWORD', '')
    db_host = os.getenv('PERSONAL_DATA_DB_HOST', 'localhost')
    db_name = os.getenv('PERSONAL_DATA_DB_NAME')

    connection = mysql.connector.connect(
        host=db_host,
        user=db_username,
        password=db_password,
        database=db_name
    )

    return connection
