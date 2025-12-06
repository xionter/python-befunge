#!/usr/bin/env python3

import sys
import argparse
from befunge93 import Befunge93


def main():
    parser = argparse.ArgumentParser()
    
    parser.add_argument(
        "file",
        help="Файл с программой Befunge (.bf)"
    )
    
    parser.add_argument(
        "-d", "--debug",
        action="store_true",
        help="Включить режим отладки"
    )
    
    parser.add_argument(
        "-s", "--steps",
        type=int,
        default=10000,
        help="Максимальное количество шагов (по умолчанию: 10000)"
    )
    
    parser.add_argument(
        "-i", "--input",
        help="Файл с входными данными (для команд & и ~)"
    )
    
    args = parser.parse_args()
    
    try:
        with open(args.file, 'r', encoding='utf-8') as f:
            code = f.read()
        
        interpreter = Befunge93(code, debug=args.debug)
        
        if args.input:
            with open(args.input, 'r', encoding='utf-8') as f:
                input_data = f.read()
        
        result = interpreter.run(max_steps=args.steps)
        
        print("\nРезультат выполнения:")
        print(result)
        
    except FileNotFoundError:
        print(f"Ошибка: файл '{args.file}' не найден", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Ошибка: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
