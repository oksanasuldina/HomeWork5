dict_lessons = {}
with open("lessons.txt", encoding="utf-8") as lessons_file:
    for line in lessons_file:
        name, hours = line.split(':')
        str_hours = ''
        for el in hours:
            if el == ' ' or ('0' <= el <= '9'):
                str_hours += el
        dict_lessons[name] = sum(map(int, str_hours.split()))
print(f"{dict_lessons}")
