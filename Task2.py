with open(' lines.txt', 'r') as lines_file:
    print(f"В файле {len(lines_file.readlines())} строки")  # возвращает список строк, len длину списка
with open(' lines.txt', 'r') as lines_file:
    for i, line in enumerate(lines_file):
        print(f"Количество слов в {i + 1} строке {len(line.split(' '))}")
