#!/usr/bin/env python3

import subprocess
import sys
import os

def run_all_tests():
    print("="*60)
    
    test_files = [
        'tests/test_basic.py',
        'tests/test_arithmetic.py',
    ]
    
    all_passed = True
    
    for test_file in test_files:
        if os.path.exists(test_file):
            print(f"\n{'='*60}")
            print(f"Запуск {test_file}")
            print('='*60)
            
            try:
                result = subprocess.run(
                    [sys.executable, test_file],
                    capture_output=False,
                    text=True,
                    timeout=10
                )
                
                if result.returncode == 0:
                    print(f"\n{test_file} - ОК")
                else:
                    print(f"\n {test_file} - ошибка(код: {result.returncode})")
                    all_passed = False
                    
            except subprocess.TimeoutExpired:
                print(f"\n {test_file} - превышено время выполнения")
                all_passed = False
            except Exception as e:
                print(f"\n {test_file} - исключение: {e}")
                all_passed = False
        else:
            print(f"\n Файл {test_file} не найден")
    
    print("\n" + "="*60)
    if all_passed:
        print("Все тесты успешно пройдены!")
    else:
        print("Некоторые тесты не прошли")
    print("="*60)
    
    return all_passed


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
