#!/usr/bin/env python3

import sys
import argparse
from befunge93 import Befunge93


def main():
    parser = argparse.ArgumentParser(
            prog="befunge",
            description="Интерпретатор Befunge-93 с пошаговым режимом и дебаггером.",
            formatter_class=argparse.RawTextHelpFormatter,
            epilog=(
                "Примеры:\n"
                "  python interpreter.py examples/hello.bf\n"
                "  python interpreter.py -d examples/arith.bf\n"
                "  python interpreter.py --step examples/loop.bf\n"
                "  python interpreter.py -i input.txt examples/io.bf\n\n"
                "Пошаговый режим:\n"
                "  Enter - следующий шаг\n"
                "  c     - продолжить выполнение\n"
                "  q     - выход\n"
        )
    )

    parser.add_argument("file", help="Файл с программой Befunge (.bf)")
    parser.add_argument("-d", "--debug", action="store_true", help="Включить режим отладки")
    parser.add_argument("-s", "--steps", type=int, default=10000,
                        help="Максимальное количество шагов (по умолчанию: 10000)")
    parser.add_argument("--step", action="store_true",
                        help="Пошаговое выполнение (ожидание нажатия клавиши)")
    parser.add_argument("-i", "--input", help="Файл с входными данными (для команд & и ~)")
    
    args = parser.parse_args()
    
    try:
        with open(args.file, 'r', encoding='utf-8') as f:
            code = f.read()
        
        interpreter = Befunge93(code, debug=args.debug)

        if args.input:
            with open(args.input, 'r', encoding='utf-8') as f:
                input_data = f.read()
            interpreter.set_input(input_data)

        if args.step:
            interpreter.step_mode = True

            while interpreter.running:
                interpreter.step()
                
                print(f"\n[STEP {interpreter.step_count}]")
                print(f"  pos=({interpreter.x}, {interpreter.y})")
                print(f"  dir=({interpreter.dx},{interpreter.dy})")
                print(f"  cmd='{interpreter.get_current_cell()}'")
                print(f"  stack={interpreter.stack}")
                print(f"  output='{''.join(interpreter.output)}'")
                
                user = input("Enter=next | c=continue | q=quit > ")

                if user.lower() == "q":
                    break
                elif user.lower() == "c":
                    interpreter.step_mode = False
                    interpreter.run(max_steps=args.steps)
                    break

            result = ''.join(interpreter.output)

        else:
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
