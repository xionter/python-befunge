#!/usr/bin/env python3

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from befunge93 import Befunge93


def test_addition():
    print("=== Тест сложения ===")
    code = "34+.@"
    interpreter = Befunge93(code, debug=False)
    result = interpreter.run()
    print(code)
    print(f"Ожидается '7 ', получено '{result}'")
    assert result == "7 ", f"Ожидается '7 ', получено '{result}'"
    print("OK")


def test_subtraction():
    print("\n=== Тест вычитания ===")
    code = "85-.@"
    interpreter = Befunge93(code, debug=False)
    result = interpreter.run()
    print(code)
    print(f"Ожидается '3 ', получено '{result}'")
    assert result == "3 ", f"Ожидается '3 ', получено '{result}'"
    print("OK")


def test_multiplication():
    print("\n=== Тест умножения ===")
    code = "34*.@"
    interpreter = Befunge93(code, debug=False)
    result = interpreter.run()
    print(code)
    print(f"Ожидается '12 ', получено '{result}'")
    assert result == "12 ", f"Ожидается '12 ', получено '{result}'"
    print("OK")


def test_division():
    print("\n=== Тест деления ===")
    code = "82/.@"
    interpreter = Befunge93(code, debug=False)
    result = interpreter.run()
    print(code)
    print(f"Ожидается '4 ', получено '{result}'")

    assert result == "4 ", f"Ожидается '4 ', получено '{result}'"
    print("OK")


def test_modulo():
    print("\n=== Тест остатка от деления ===")
    code = "73%.@"
    interpreter = Befunge93(code, debug=False)
    result = interpreter.run()
    print(code)
    print(f"Ожидается '1 ', получено '{result}'")

    assert result == "1 ", f"Ожидается '1 ', получено '{result}'"
    print("OK")


def test_complex_expression():
    print("\n=== Тест комплексного выражения ===")
    code = "34*2+.@"
    interpreter = Befunge93(code, debug=False)
    result = interpreter.run()
    print(code)
    print(f"Ожидается '14 ', получено '{result}'")

    assert result == "14 ", f"Ожидается '14 ', получено '{result}'"
    print("OK")


if __name__ == "__main__":
    test_addition()
    test_subtraction()
    test_multiplication()
    test_division()
    test_modulo()
    test_complex_expression()
    print("\nВсе арифметические тесты пройдены!")
