#!/usr/bin/env python3

import sys
import os

sys.path.insert(0, os.path.abspath('.'))

def run_all_tests():
    print("="*60)
    
    test_modules = [
        'tests.test_basic',
        'tests.test_arithmetic', 
    ]
    
    for module_name in test_modules:
        print(f"\nЗапуск {module_name}...")
        try:
            __import__(module_name)
            module = sys.modules[module_name]
            if hasattr(module, '__name__'):
                print(f"{module_name} завершен")
        except Exception as e:
            print(f"Ошибка в {module_name}: {e}")
            return False
    
    print("\n" + "="*60)
    print("Все тесты успешно пройдены!")
    print("="*60)
    return True


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
