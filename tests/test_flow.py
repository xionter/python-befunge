#!/usr/bin/env python3
import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from befunge93 import Befunge93

def test_horizontal_if():
    code = "0_7.@1.@"
    result = Befunge93(code).run()
    assert result == "7 ", f"Ожидается '7 ', получено '{result}'"


def test_vertical_if():
    code = (
        "0|\n"
        "v>4.@"
    )


    result = Befunge93(code).run()
    assert result == "4 ", f"Ожидается '4 ', получено '{result}'"

if __name__ == "__main__":
    test_horizontal_if()
    test_vertical_if()
    print("OK: условные переходы")

