import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from math_module import multiply

def test_multiply():
    assert multiply(6, 7) == 42
