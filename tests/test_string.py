#!/usr/bin/env python3
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from befunge93 import Befunge93

def test_string_mode():
    code = '"!iH",,,@'
    interpreter = Befunge93(code)
    result = interpreter.run()
    assert result == "Hi!", f"Ожидается 'Hi!', получено '{result}'"
    print("OK: строковый режим")

if __name__ == "__main__":
    test_string_mode()

