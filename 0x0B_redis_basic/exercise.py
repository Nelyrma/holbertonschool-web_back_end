#!/usr/bin/env python3
"""exercise module"""

import redis
import uuid
from typing import Union


class Cache:
    """the Cache class"""
    def __init__(self):
        """initialize the Redis client"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """generate a random key"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)

        return key
