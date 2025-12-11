#!/usr/bin/env python3
import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from befunge93 import Befunge93

def test_skip():
    code = "1#2.@"
    result = Befunge93(code).run()
    assert result == "1 ", f"Ожидается '1 ', получено '{result}'"

if __name__ == "__main__":
    test_skip()
    print("OK: оператор #")

