numbers = '1 85 35 6 18 -1'
summa = 0
with open('numbers.txt', mode='w+', encoding='utf-8') as numbers_file:
    numbers_file.write(numbers)
with open('numbers.txt', 'r', encoding='utf-8') as numbers_file:
    for line in numbers_file:
        numbers_from_file = line.split(' ')
        for el in numbers_from_file:
            summa += int(el)
        print(f"Сумма чисел в файле: {summa}")









