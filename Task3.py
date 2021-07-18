with open('staff.txt', 'r') as data:
    print('Сотрудники с окладом менее 20 тыс. руб.: ')
    for i, line in enumerate(data):
        staff = line.split(' ')
        if int(staff[1]) < 20000:
            print(staff[0])
count = 0
with open('staff.txt', 'r') as data:
    count = len(data.readlines())
with open('staff.txt', 'r') as data:
    sum_salary = 0
    for i, line in enumerate(data):
        staff = line.split(' ')
        sum_salary += int(staff[1])
    print(f"Средняя величина дохода сотрудников: {sum_salary/count} тыс. руб. ")
