#!/usr/bin/env python3
import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from befunge93 import Befunge93

def test_put_get():
    code = '"A"00p00g,@'
    result = Befunge93(code).run()
    assert result == "A", f"Ожидается 'A', получено '{result}'"
    print("OK: p/g")

if __name__ == "__main__":
    test_put_get()

