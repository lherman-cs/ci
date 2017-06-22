import os
import sys

from ci import get_hello


def test_get_hello():
    assert get_hello() == "hello"
