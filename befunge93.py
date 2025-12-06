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
            if char == '"':
                self.string_mode = False
                self.log("Выход из строкового режима")
            else:
                self.push(ord(char))
                self.log(f"Добавлен символ '{char}' (код {ord(char)}) в стек")
        else:
            if char == ' ':
                self.log("Пробел - пропускаем")
                pass
            elif char == '@':
                self.log("Команда '@' - завершение программы")
                self.running = False
                return False
            
            elif char == '>':
                self.dx, self.dy = 1, 0
                self.log("Направление: вправо")
            elif char == '<':
                self.dx, self.dy = -1, 0
                self.log("Направление: влево")
            elif char == '^':
                self.dx, self.dy = 0, -1
                self.log("Направление: вверх")
            elif char == 'v':
                self.dx, self.dy = 0, 1
                self.log("Направление: вниз")
                
            elif char == '?':
                dirs = [(1, 0), (-1, 0), (0, -1), (0, 1)]
                self.dx, self.dy = random.choice(dirs)
                self.log(f"Случайное направление: ({self.dx}, {self.dy})")
            
            elif '0' <= char <= '9':
                self.push(int(char))
                self.log(f"Добавлено число {char} в стек")
            
            elif char == '+':
                a = self.pop()
                b = self.pop()
                self.push(b + a)
                self.log(f"Сложение: {b} + {a} = {b + a}")
            elif char == '-':
                a = self.pop()
                b = self.pop()
                self.push(b - a)
                self.log(f"Вычитание: {b} - {a} = {b - a}")
            elif char == '*':
                a = self.pop()
                b = self.pop()
                self.push(b * a)
                self.log(f"Умножение: {b} * {a} = {b * a}")
            elif char == '/':
                a = self.pop()
                b = self.pop()
                if a == 0:
                    self.push(0)
                    self.log(f"Деление на ноль: 0")
                else:
                    self.push(b // a)
                    self.log(f"Деление: {b} / {a} = {b // a}")
            elif char == '%':
                a = self.pop()
                b = self.pop()
                if a == 0:
                    self.push(0)
                    self.log(f"Остаток от деления на ноль: 0")
                else:
                    self.push(b % a)
                    self.log(f"Остаток: {b} % {a} = {b % a}")
            
            elif char == '!':
                a = self.pop()
                result = 1 if a == 0 else 0
                self.push(result)
                self.log(f"Логическое НЕ: {a} -> {result}")
            elif char == '`':
                a = self.pop()
                b = self.pop()
                result = 1 if b > a else 0
                self.push(result)
                self.log(f"Сравнение 'больше': {b} > {a} = {result}")
            
            elif char == ':':
                if self.stack:
                    a = self.stack[-1]
                    self.push(a)
                    self.log(f"Дублирование: {a} -> [{a}, {a}]")
                else:
                    self.push(0)
                    self.push(0)
                    self.log("Дублирование пустого стека: [0, 0]")
            elif char == '\\':
                if len(self.stack) >= 2:
                    a = self.stack.pop()
                    b = self.stack.pop()
                    self.stack.append(a)
                    self.stack.append(b)
                    self.log(f"Обмен: [{b}, {a}] -> [{a}, {b}]")
                elif len(self.stack) == 1:
                    a = self.stack.pop()
                    self.stack.append(0)
                    self.stack.append(a)
                    self.log(f"Обмен с одним элементом: [{a}] -> [{a}, 0]")
                else:
                    self.stack.append(0)
                    self.stack.append(0)
                    self.log("Обмен пустого стека: [0, 0]")
            elif char == '$':
                a = self.pop()
                self.log(f"Выталкивание: удалено {a}")
            
            elif char == '_':
                a = self.pop()
                if a == 0:
                    self.dx, self.dy = 1, 0
                    self.log(f"Условное вправо (0): {a} -> движение вправо")
                else:
                    self.dx, self.dy = -1, 0
                    self.log(f"Условное вправо (не 0): {a} -> движение влево")
            elif char == '|':
                a = self.pop()
                if a == 0:
                    self.dx, self.dy = 0, 1
                    self.log(f"Условное вниз (0): {a} -> движение вниз")
                else:
                    self.dx, self.dy = 0, -1
                    self.log(f"Условное вниз (не 0): {a} -> движение вверх")
            
            elif char == '"':
                self.string_mode = True
                self.log("Вход в строковый режим")
            
            elif char == '#':
                self.move_pointer()
                self.log("Пропуск следующей ячейки (#)")
            
            elif char == '&':
                try:
                    val = int(input("Введите число: "))
                    self.push(val)
                    self.log(f"Ввод числа: {val}")
                except ValueError:
                    self.push(0)
                    self.log("Неверный ввод, положен 0")
            elif char == '~':
                inp = input("Введите символ: ")
                if inp:
                    self.push(ord(inp[0]))
                    self.log(f"Ввод символа: '{inp[0]}' (код {ord(inp[0])})")
                else:
                    self.push(0)
                    self.log("Пустой ввод, положен 0")
            
            elif char == 'p':
                y = self.pop()
                x = self.pop()
                v = self.pop()
                if 0 <= y < self.height and 0 <= x < self.width:
                    self.grid[y][x] = chr(v % 256)
                    self.log(f"Запись в поле: ({x}, {y}) = '{chr(v % 256)}'")
                else:
                    self.log(f"Запись за пределами поля: ({x}, {y})")
            elif char == 'g':
                y = self.pop()
                x = self.pop()
                if 0 <= y < self.height and 0 <= x < self.width:
                    val = ord(self.grid[y][x])
                    self.push(val)
                    self.log(f"Чтение из поля: ({x}, {y}) = '{self.grid[y][x]}' (код {val})")
                else:
                    self.push(0)
                    self.log(f"Чтение за пределами поля: ({x}, {y})")
            
            elif char == '.':
                value = self.pop()
                self.output.append(str(value) + ' ')
                self.log(f"Вывод числа: {value}")
            elif char == ',':
                value = self.pop()
                self.output.append(chr(value % 256))
                self.log(f"Вывод символа: '{chr(value % 256)}' (код {value})")
            
            else:
                self.log(f"Неизвестная команда: '{char}'")
        
        if char != '#':
            self.move_pointer()
        
        if self.debug:
            print(f"Стек после: {self.stack}")
            print(f"Новая позиция: ({self.x}, {self.y})\n")
        
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
