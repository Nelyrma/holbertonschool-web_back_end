#!/usr/bin/env python3
"""exercise module"""

import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """define the count_calls decorator"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """count how many times methods of
        the Cache class are called"""
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """define the count_history decorator"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """store the history of inputs and outputs
        for a particular function"""
        inputs_key = f"{method.__qualname__}:inputs"
        outputs_key = f"{method.__qualname__}:outputs"

        self._redis.rpush(inputs_key, str(args))
        output = method(self, *args)
        self._redis.rpush(outputs_key, output)
        return output
    return wrapper


def replay(method) -> None:
    """display the history of calls of a particular function"""
    local_redis = redis.Redis()

    inputs_key = f"{method.__qualname__}:inputs"
    outputs_key = f"{method.__qualname__}:outputs"

    inputs_history = local_redis.lrange(inputs_key, 0, -1)
    outputs_history = local_redis.lrange(outputs_key, 0, -1)

    result = list(zip(inputs_history, outputs_history))

    print("{} was called {} times:".format(method.__qualname__,
                                           len(result)))

    for item in result:
        print("{}(*{}) -> {}".format(method.__qualname__,
                                     item[0].decode(),
                                     item[1].decode()))


class Cache:
    """the Cache class"""
    def __init__(self):
        """initialize the Redis client"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """generate a random key"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)

        return key

    def get(self, key: str, fn: Optional[Callable] = None) \
            -> Union[str, bytes, int, float]:
        """recover data from Redis"""
        data = self._redis.get(key)
        if data is None:
            return None

        if fn:
            data = fn(data)

        return data

    def get_str(self, key: str) -> str:
        """use get with a conversion function in UTF-8 string"""
        return self.get(key, lambda value: value.decode("utf-8"))

    def get_int(self, key: str) -> int:
        """use get with a conversion function in integer"""
        return self.get(key, int)
