#!/usr/bin/env python3

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from befunge93 import Befunge93


def test_simple_output():
    print("=== Тест 1: Простой вывод числа ===")
    code = "5.@"
    interpreter = Befunge93(code)
    result = interpreter.run()
    assert result == "5 ", f"Ожидается '5 ', получено '{result}'"
    print("OK")


def test_multiple_numbers():
    print("\n=== Тест 2: Несколько чисел ===")
    code = "52..@"
    interpreter = Befunge93(code)
    result = interpreter.run()
    assert result == "2 5 ", f"Ожидается '2 5 ', получено '{result}'"
    print("OK")


def test_movement():
    print("\n=== Тест 3: Движение вправо ===")
    code = ">5.@"
    interpreter = Befunge93(code)
    result = interpreter.run()
    assert result == "5 ", f"Ожидается '5 ', получено '{result}'"
    print("OK")


if __name__ == "__main__":
    test_simple_output()
    test_multiple_numbers()
    test_movement()
    print("\nВсе базовые тесты пройдены!")
