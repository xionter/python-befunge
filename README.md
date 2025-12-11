# Интерпретатор Befunge-93

## Описание
Простой интерпретатор языка Befunge-93, написанный на Python.  
Поддерживает выполнение 2D-кода, пошаговый режим и базовый режим отладки.  
Реализованы все стандартные команды Befunge-93, включая арифметику, стековые операции, ветвления, ввод/вывод и работу с полем (`p`/`g`).

---

## Использование

Запуск программы Befunge:

```bash
python interpreter.py <program.bf>
```

Просмотр справки:

```bash
python interpreter.py -h
```

Пример запуска с отладкой:

```bash
python interpreter.py --debug examples/hello.bf
```

Пошаговый режим:

```bash
python interpreter.py --step examples/hello.bf
```

Запуск с входными данными:

```bash
python interpreter.py -i input.txt examples/hello.bf
```
