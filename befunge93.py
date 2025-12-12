#!/usr/bin/env python3

import random


class Befunge93:
    def __init__(self, source_code, debug=False):
        lines = source_code.rstrip('\n').split('\n')
        
        self.width = max(len(line) for line in lines) if lines else 0
        self.height = len(lines)
        
        self.grid = []
        for line in lines:
            row = list(line.ljust(self.width, ' '))
            self.grid.append(row)
        
        self.stack = []           
        self.x = 0                
        self.y = 0                
        self.dx = 1              
        self.dy = 0               
        self.string_mode = False  
        self.running = True       
        self.output = []          
        self.debug = debug        
        self.step_count = 0       
        self.input_buffer = []
        self.step_mode = False

        
    def get_current_cell(self):
        return self.grid[self.y][self.x]
    
    def move_pointer(self):
        self.x += self.dx
        self.y += self.dy
        
        if self.x >= self.width:
            self.x = 0
        elif self.x < 0:
            self.x = self.width - 1
            
        if self.y >= self.height:
            self.y = 0
        elif self.y < 0:
            self.y = self.height - 1
    
    def pop(self):
        return self.stack.pop() if self.stack else 0
    
    def push(self, value):
        self.stack.append(int(value))
    
    def set_input(self, input_data):
        self.input_buffer = list(input_data)
    
    def read_char(self):
        if self.input_buffer:
            return self.input_buffer.pop(0)
        return None
    
    def log(self, message):
        if self.debug:
            print(f"[Шаг {self.step_count}] {message}")
    
    def step(self):
        if not self.running:
            return False

        self.step_count += 1
        char = self.get_current_cell()

        if self.string_mode:
            match char:
                case '"':
                    self.string_mode = False
                    self.log("Выход из строкового режима")
                case _:
                    self.push(ord(char))
                    self.log(f"Строковый режим: push '{char}' ({ord(char)})")
            self.move_pointer()
            return True

        match char:

            case ' ':
                self.log("Пробел - пропуск")

            case '@':
                self.log("Завершение программы '@'")
                self.running = False
                return False

            case '>':
                self.dx, self.dy = 1, 0
                self.log("Движение вправо")
            case '<':
                self.dx, self.dy = -1, 0
                self.log("Движение влево")
            case '^':
                self.dx, self.dy = 0, -1
                self.log("Движение вверх")
            case 'v':
                self.dx, self.dy = 0, 1
                self.log("Движение вниз")

            case '?':
                dirs = [(1,0), (-1,0), (0,-1), (0,1)]
                self.dx, self.dy = random.choice(dirs)
                self.log(f"Случайное направление {self.dx, self.dy}")

            case d if d.isdigit():
                self.push(int(d))
                self.log(f"push {d}")

            case '+':
                a, b = self.pop(), self.pop()
                self.push(b + a)
                self.log(f"{b} + {a}")
            case '-':
                a, b = self.pop(), self.pop()
                self.push(b - a)
                self.log(f"{b} - {a}")
            case '*':
                a, b = self.pop(), self.pop()
                self.push(b * a)
                self.log(f"{b} * {a}")
            case '/':
                a, b = self.pop(), self.pop()
                self.push(0 if a == 0 else b // a)
                self.log(f"{b} / {a}")
            case '%':
                a, b = self.pop(), self.pop()
                self.push(0 if a == 0 else b % a)
                self.log(f"{b} % {a}")

            case '!':
                a = self.pop()
                self.push(1 if a == 0 else 0)
                self.log(f"!{a}")
            case '`':
                a, b = self.pop(), self.pop()
                self.push(1 if b > a else 0)
                self.log(f"{b} > {a}")

            case ':':
                if self.stack:
                    self.push(self.stack[-1])
                    self.log("Дублирование")
                else:
                    self.push(0); self.push(0)
                    self.log("Дубликат пустого стека -> 0,0")

            case '\\':
                match len(self.stack):
                    case 0:
                        self.push(0); self.push(0)
                        self.log("swap пустого стека -> 0,0")
                    case 1:
                        a = self.pop()
                        self.push(0); self.push(a)
                        self.log("swap одного элемента")
                    case _:
                        a = self.stack.pop()
                        b = self.stack.pop()
                        self.stack.append(a)
                        self.stack.append(b)
                        self.log(f"swap {b} <-> {a}")

            case '$':
                x = self.pop()
                self.log(f"pop {x}")

            case '_':
                a = self.pop()
                self.dx, self.dy = (1,0) if a == 0 else (-1,0)
                self.log(f"_ -> {self.dx, self.dy}")
            case '|':
                a = self.pop()
                self.dx, self.dy = (0,1) if a == 0 else (0,-1)
                self.log(f"| -> {self.dx, self.dy}")

            case '"':
                self.string_mode = True
                self.log("Вход в строковый режим")

            case '#':
                self.move_pointer()
                self.log("Пропуск '#'")

            case '&':
                try:
                    v = int(input("Введите число: "))
                except ValueError:
                    v = 0
                self.push(v)
                self.log(f"Ввод & : {v}")

            case '~':
                s = input("Введите символ: ")
                self.push(ord(s[0]) if s else 0)
                self.log(f"Ввод ~ : {s}")

            case 'p':
                y, x, v = self.pop(), self.pop(), self.pop()
                if 0 <= x < self.width and 0 <= y < self.height:
                    self.grid[y][x] = chr(v % 256)
                    self.log(f"grid[{y},{x}] = '{chr(v%256)}'")
                else:
                    self.log("p вне границ")

            case 'g':
                y, x = self.pop(), self.pop()
                if 0 <= x < self.width and 0 <= y < self.height:
                    val = ord(self.grid[y][x])
                else:
                    val = 0
                self.push(val)
                self.log(f"g → {val}")

            case '.':
                v = self.pop()
                self.output.append(str(v) + ' ')
                self.log(f"вывод числа {v}")

            case ',':
                v = self.pop()
                self.output.append(chr(v % 256))
                self.log(f"вывод символа '{chr(v%256)}'")

            case _:
                self.log(f"Неизвестная команда '{char}'")

        self.move_pointer()

        if self.debug:
            print(f"Стек: {self.stack}")
            print(f"Позиция: {self.x, self.y}")

        return True

    def run(self, max_steps=10000):
        steps = 0
        while self.running and steps < max_steps:
            if not self.step():
                break
            steps += 1
        
        if steps >= max_steps:
            if self.debug:
                print(f"Достигнут лимит шагов: {max_steps}")
        
        return ''.join(self.output)
