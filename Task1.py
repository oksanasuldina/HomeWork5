print('Запишем в файл список нужных покупок, для окончания записи введите пустую строку: ')
with open('shopping_list.txt', 'w', encoding='utf-8') as shopping_list_file:
    while True:
        purchase = input('введите покупку: ')
        if purchase == '':
            break
        shopping_list_file.write(purchase + '\n')
print('Готово. Список записан в файл. ')
