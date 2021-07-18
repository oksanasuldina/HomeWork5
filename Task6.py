dict_lessons = {}
with open("lessons.txt", encoding="utf-8") as lessons_file:
    for line in lessons_file:
        name, hours = line.split(':')
        name_sum = sum(map(int, "".join([i for i in hours if i == ' ' or ('0' <= i <= '9')]).split()))
        dict_lessons[name] = name_sum
print(f"{dict_lessons}")
