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

    def get(self, key: str, fn: Optional[Callable] = None) \
            -> Optional[Union[str, bytes, int, float]]:
        """recover data from Redis"""
        data = self._redis.get(key)
        if data is None:
            return None
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> Optional[str]:
        """use get with a conversion function in UTF-8 string"""
        return self.get(key, lambda value: value.decode("utf-8"))

    def get_int(self, key: str) -> Optional[int]:
        """use get with a conversion function in integer"""
        return self.get(key, fn=int)
