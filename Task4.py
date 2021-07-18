numerals = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
with open('numerals.txt', 'r', encoding='utf-8') as data_file, \
        open('numerals_new.txt', 'w', encoding='utf-8') as new_data_file:
    for i, line in enumerate(data_file):
        number = line.split(' — ')
        new_data_file.write(numerals.get(number[0]) + ' — ' + number[1])
print('Готово. Проверьте numerals_new.txt ')




