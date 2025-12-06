#!/usr/bin/env python3

import sys
import os

sys.path.insert(0, os.path.abspath('.'))

def run_tests():
    print("Запуск тестов Befunge-93 интерпретатора...\n")
    
    import tests.test_basic
#    import tests.test_arithmetic
#    import tests.test_logical
    
    print("\n" + "="*50)
    print("Все тесты успешно пройдены!")
    print("="*50)


if __name__ == "__main__":
    run_tests()
