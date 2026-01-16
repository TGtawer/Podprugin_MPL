import re

class PascalToPythonTranslator:
    def __init__(self):
        self.python_code = ""

    def translate(self, pascal_code):
        lines = pascal_code.splitlines()
        py_lines = []

        indent = 0
        skip_var_block = False
        save_else_indent = False
        prev_row_was_else = False
        prev_row_was_if = False
        prev_row_was_cycle = False

        for line in lines:
            line = line.strip()

            if not line:
                if len(py_lines) > 0 and py_lines[-1] != "":
                    py_lines.append("")
                continue

            if line.lower().startswith("var"):
                skip_var_block = True
                continue
            if skip_var_block:
                if line.lower() == "begin":
                    skip_var_block = False
                else:
                    continue  

            proc_match = re.match(r'(procedure|function)\s+(\w+)', line, re.I)
            if proc_match:
                name = proc_match.group(2)
                py_lines.append(" " * (indent*4) + f"def {name}():")
                indent += 1
                continue
            
            if line.lower() == "begin":
                prev_row_was_else = False
                prev_row_was_if = False
                prev_row_was_cycle = False
                continue
            if line.lower().startswith("end"):
                indent -= 1
                save_else_indent = True
                continue

            line = re.sub(r'{(.*?)}', r'# \1', line)

            line = re.sub(r'writeln\((.*)\)\s*;?', r'print(\1)', line, flags=re.I)

            line = re.sub(r'true', 'True', line)
            line = re.sub(r'false', 'False', line)

            line = re.sub(r' mod ', ' % ', line) 
            line = re.sub(r' div ', ' // ', line)  

            line = re.sub(r'\s=\s', ' == ', line)

            match_for = re.match(r'for\s+(\w+)\s*:=\s*(.+?)\s+to\s+(.+?)\s+do', line, re.I)
            if match_for:
                var, start, end = match_for.groups()
                py_lines.append(" " * (indent*4) + f"for {var} in range({start}, {end}+1):")
                indent += 1
                prev_row_was_cycle = True
                continue
            
            match_while = re.match(r'while (.+) do', line, re.I)
            if match_while:
                condition = match_while.group(1)
                py_lines.append(" " * (indent*4) + f"while {condition}:")
                indent += 1
                prev_row_was_cycle = True
                continue

            if_match = re.match(r'if (.+) then', line, re.I)
            else_match = re.match(r'else', line, re.I)

            if if_match:
                py_lines.append(" " * (indent*4) + f"if {if_match.group(1)}:")
                indent += 1
                prev_row_was_if = True
                continue
            if else_match:
                if save_else_indent:
                    indent += 1
                indent -= 1
                py_lines.append(" " * (indent*4) + "else:")
                indent += 1
                prev_row_was_else = True
                continue   

            line = re.sub(r':=', '=', line)      

            py_lines.append(" " * (indent*4) + line)

            save_else_indent = False
            if prev_row_was_else:
                indent -= 1
                prev_row_was_else = False
            elif prev_row_was_if:
                indent -= 1
                prev_row_was_if = False
                save_else_indent = True
            elif prev_row_was_cycle:
                indent -= 1
                prev_row_was_cycle = False


        self.python_code += "\n".join(py_lines) + "\n\n"

compute_fact = """
procedure compute_fact;

var
  i, j, fact, n, sumSteps: integer;
  sumFactorials: integer;
  maxFactorial: integer;
  minFactorial: integer;
  averageFactorial: real;

begin
  n := 10;
  sumFactorials := 0;
  maxFactorial := 0;
  minFactorial := 0;

  writeln('Вычисление факториалов от 1 до ', n);
  writeln('--------------------------------');

  for i := 1 to n do
  begin
    fact := 1;
    sumSteps := 0;
    writeln('Факториал числа ', i, ':');

    for j := 1 to i do
    begin
      fact := fact * j;
      sumSteps := sumSteps + fact;
      writeln(' Шаг ', j, ': факториал = ', fact, ', сумма шагов = ', sumSteps);

      if fact mod 2 = 0 then
        writeln('  Четный факториал')
      else
        writeln('  Нечетный факториал');
    end;

    sumFactorials := sumFactorials + fact;

    if i = 1 then
      minFactorial := fact;

    if fact > maxFactorial then
      maxFactorial := fact;

    if fact < minFactorial then
      minFactorial := fact;

    if i mod 2 = 0 then
      writeln('Завершен четный факториал для i=', i)
    else 
      writeln('Завершен нечетный факториал для i=', i);

    writeln('  Квадрат факториала: ', fact*fact);
    writeln('  Куб факториала: ', fact*fact*fact);
    writeln('  i*i = ', i*i, ', i*i*i = ', i*i*i);
    writeln('  i + факториал = ', i+fact, ', факториал - i = ', fact-i);
    writeln('  sumSteps mod 3 = ', sumSteps mod 3);
    writeln('  sumSteps div 5 = ', sumSteps div 5);
    writeln('  -------------------------');
  end;

  if n > 0 then
    averageFactorial := sumFactorials / n
  else
    averageFactorial := 0;

  writeln('Сводная статистика:');
  writeln('  Сумма всех факториалов: ', sumFactorials);
  writeln('  Максимальный факториал: ', maxFactorial);
  writeln('  Минимальный факториал: ', minFactorial);
  writeln('  Среднее значение факториалов: ', averageFactorial);

  if sumFactorials mod 2 = 0 then
    writeln('Общая сумма факториалов - четная')
  else
    writeln('Общая сумма факториалов - нечетная');

  writeln('Выполнение завершено.');
end;
"""
compute_sum = """
procedure compute_sum;

var
  i, j, sum, n: integer;
  square, cube: integer;
  fact: integer;
  sumSquares: integer;
  sumCubes: integer;
  evenCount: integer;
  oddCount: integer;
  average: real;

begin
  n := 20;
  sum := 0;
  sumSquares := 0;
  sumCubes := 0;
  evenCount := 0;
  oddCount := 0;

  writeln('Суммирование чисел от 1 до ', n);
  writeln('----------------------------');

  for i := 1 to n do
  begin
    sum := sum + i;
    square := i * i;
    cube := i * i * i;
    sumSquares := sumSquares + square;
    sumCubes := sumCubes + cube;

    writeln('Число: ', i, ', текущая сумма: ', sum);
    writeln('  Квадрат: ', square, ', Куб: ', cube);

    if i mod 2 = 0 then
    begin
      evenCount := evenCount + 1;
      writeln('  Четное число');
    end
    else
    begin
      oddCount := oddCount + 1;
      writeln('  Нечетное число');
    end;

    if i mod 3 = 0 then
      writeln('   Делится на 3');

    if i mod 5 = 0 then
      writeln('   Делится на 5');

    if i mod 7 = 0 then
      writeln('   Делится на 7');

    writeln('   i + сумма = ', i + sum, ', сумма - i = ', sum - i);
    writeln('   i * сумма = ', i * sum);
    writeln('   -------------------------');
  end;

  if n > 0 then
    average := sum / n
  else
    average := 0;

  writeln('Сводная статистика:');
  writeln('  Общая сумма: ', sum);
  writeln('  Сумма квадратов: ', sumSquares);
  writeln('  Сумма кубов: ', sumCubes);
  writeln('  Среднее значение: ', average);
  writeln('  Количество четных чисел: ', evenCount);
  writeln('  Количество нечетных чисел: ', oddCount);

  writeln('Вычисление дополнительных факториалов:');

  for i := 1 to 5 do
  begin
    fact := 1;

    for j := 1 to i do
      fact := fact * j;

    writeln('  Факториал числа ', i, ' = ', fact);
  end;

  writeln('Выполнение завершено.');
end;
"""

Fibon_sub = """
procedure PrimesFoo;

var
  i, j, countPrimes: integer;
  sumPrimes: integer;
  maxPrime: integer;
  isPrime: boolean;
  divisorCount: integer;
  averagePrime: real;

begin
  countPrimes := 0;
  sumPrimes := 0;
  maxPrime := 0;

  writeln('Поиск простых чисел от 2 до 50');
  writeln('----------------------------------');

  for i := 2 to 50 do
  begin
    isPrime := true;
    divisorCount := 0;

    for j := 2 to i-1 do
    begin
      if i mod j = 0 then
      begin
        isPrime := false;
        divisorCount := divisorCount + 1;
        writeln(i, ' делится на ', j);
      end;
    end;

    if isPrime then
    begin
      writeln(i, ' - простое число');
      countPrimes := countPrimes + 1;
      sumPrimes := sumPrimes + i;
      maxPrime := i;
    end
    else
      writeln(i, ' - не является простым числом');

    writeln('  количество делителей = ', divisorCount);
    writeln('  i в квадрате = ', i*i, ', i в кубе = ', i*i*i);
    writeln('  i mod 2 = ', i mod 2, ', i mod 3 = ', i mod 3);
    writeln('  -------------------------');
  end;

  if countPrimes > 0 then
    averagePrime := sumPrimes / countPrimes
  else
    averagePrime := 0;

  writeln('Всего найдено простых чисел: ', countPrimes);
  writeln('Сумма простых чисел: ', sumPrimes);
  writeln('Наибольшее простое число: ', maxPrime);
  writeln('Среднее значение простых чисел: ', averagePrime);

  if countPrimes mod 2 = 0 then
    writeln('Количество простых чисел - четное')
  else
    writeln('Количество простых чисел - нечетное');

  writeln('Выполнение завершено.');
end;
"""

translator = PascalToPythonTranslator()
translator.translate(compute_fact)
translator.translate(compute_sum)
translator.translate(Fibon_sub)

with open("python_res.py", "w", encoding="utf-8") as f:
    f.write(translator.python_code)

print("Successful")