import sys
import os
sys.path.insert(1, os.path.abspath('..'))

from main import get_hello


def test_get_hello():
    assert get_hello() == "hello"
