def compute_fact():

    n = 10;
    sumFactorials = 0;
    maxFactorial = 0;
    minFactorial = 0;

    print('Вычисление факториалов от 1 до ', n)
    print('--------------------------------')

    for i in range(1, n+1):
        fact = 1;
        sumSteps = 0;
        print('Факториал числа ', i, ':')

        for j in range(1, i+1):
            fact = fact * j;
            sumSteps = sumSteps + fact;
            print(' Шаг ', j, ': факториал == ', fact, ', сумма шагов == ', sumSteps)

            if fact % 2 == 0:
                print('  Четный факториал')
            else:
                print('  Нечетный факториал')

        sumFactorials = sumFactorials + fact;

        if i == 1:
            minFactorial = fact;

        if fact > maxFactorial:
            maxFactorial = fact;

        if fact < minFactorial:
            minFactorial = fact;

        if i % 2 == 0:
            print('Завершен четный факториал для i=', i)
        else:
            print('Завершен нечетный факториал для i=', i)

        print('  Квадрат факториала: ', fact*fact)
        print('  Куб факториала: ', fact*fact*fact)
        print('  i*i == ', i*i, ', i*i*i == ', i*i*i)
        print('  i + факториал == ', i+fact, ', факториал - i == ', fact-i)
        print('  sumSteps % 3 == ', sumSteps % 3)
        print('  sumSteps // 5 == ', sumSteps // 5)
        print('  -------------------------')

    if n > 0:
        averageFactorial = sumFactorials / n
    else:
        averageFactorial = 0;

    print('Сводная статистика:')
    print('  Сумма всех факториалов: ', sumFactorials)
    print('  Максимальный факториал: ', maxFactorial)
    print('  Минимальный факториал: ', minFactorial)
    print('  Среднее значение факториалов: ', averageFactorial)

    if sumFactorials % 2 == 0:
        print('Общая сумма факториалов - четная')
    else:
        print('Общая сумма факториалов - нечетная')

    print('Выполнение завершено.')

def compute_sum():

    n = 20;
    sum = 0;
    sumSquares = 0;
    sumCubes = 0;
    evenCount = 0;
    oddCount = 0;

    print('Суммирование чисел от 1 до ', n)
    print('----------------------------')

    for i in range(1, n+1):
        sum = sum + i;
        square = i * i;
        cube = i * i * i;
        sumSquares = sumSquares + square;
        sumCubes = sumCubes + cube;

        print('Число: ', i, ', текущая сумма: ', sum)
        print('  Квадрат: ', square, ', Куб: ', cube)

        if i % 2 == 0:
            evenCount = evenCount + 1;
            print('  Четное число')
        else:
            oddCount = oddCount + 1;
            print('  Нечетное число')

        if i % 3 == 0:
            print('   Делится на 3')

        if i % 5 == 0:
            print('   Делится на 5')

        if i % 7 == 0:
            print('   Делится на 7')

        print('   i + сумма == ', i + sum, ', сумма - i == ', sum - i)
        print('   i * сумма == ', i * sum)
        print('   -------------------------')

    if n > 0:
        average = sum / n
    else:
        average = 0;

    print('Сводная статистика:')
    print('  Общая сумма: ', sum)
    print('  Сумма квадратов: ', sumSquares)
    print('  Сумма кубов: ', sumCubes)
    print('  Среднее значение: ', average)
    print('  Количество четных чисел: ', evenCount)
    print('  Количество нечетных чисел: ', oddCount)

    print('Вычисление дополнительных факториалов:')

    for i in range(1, 5+1):
        fact = 1;

        for j in range(1, i+1):
            fact = fact * j;

        print('  Факториал числа ', i, ' == ', fact)

    print('Выполнение завершено.')

def PrimesFoo():

    countPrimes = 0;
    sumPrimes = 0;
    maxPrime = 0;

    print('Поиск простых чисел от 2 до 50')
    print('----------------------------------')

    for i in range(2, 50+1):
        isPrime = True;
        divisorCount = 0;

        for j in range(2, i-1+1):
            if i % j == 0:
                isPrime = False;
                divisorCount = divisorCount + 1;
                print(i, ' делится на ', j)

        if isPrime:
            print(i, ' - простое число')
            countPrimes = countPrimes + 1;
            sumPrimes = sumPrimes + i;
            maxPrime = i;
        else:
            print(i, ' - не является простым числом')

        print('  количество делителей == ', divisorCount)
        print('  i в квадрате == ', i*i, ', i в кубе == ', i*i*i)
        print('  i % 2 == ', i % 2, ', i % 3 == ', i % 3)
        print('  -------------------------')

    if countPrimes > 0:
        averagePrime = sumPrimes / countPrimes
    else:
        averagePrime = 0;

    print('Всего найдено простых чисел: ', countPrimes)
    print('Сумма простых чисел: ', sumPrimes)
    print('Наибольшее простое число: ', maxPrime)
    print('Среднее значение простых чисел: ', averagePrime)

    if countPrimes % 2 == 0:
        print('Количество простых чисел - четное')
    else:
        print('Количество простых чисел - нечетное')

    print('Выполнение завершено.')

PrimesFoo()
compute_fact()
compute_sum()