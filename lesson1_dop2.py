from collections import Counter
task="Задание 1"
print(task)
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика.
students = [
	{'first_name': 'Вася'},
	{'first_name': 'Петя'},
	{'first_name': 'Маша'},
	{'first_name': 'Маша'},
	{'first_name': 'Петя'},
]

# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

sort_list=[]
for x in students:
	sort_var=x.get('first_name')
	sort_list.append(sort_var)
count=Counter(sort_list)
for y in count:
	text="# {}: {}".format(y, count[y])
	print(text)

task="Задание 2"
print(task)
# Дан список учеников, нужно вывести самое часто повторящееся имя.

students = [
	{'first_name': 'Вася'},
	{'first_name': 'Петя'},
	{'first_name': 'Маша'},
	{'first_name': 'Маша'},
	{'first_name': 'Оля'},
]

# Пример вывода:
# Самое частое имя среди учеников: Маша

sort_list=[]
for x in students:
	sort_var=x.get('first_name')
	sort_list.append(sort_var)
count=Counter(sort_list).most_common(1)[0]
print("Самое распространенное имя среди учеников: {}".format(count[0]))

task="Задание 3"
print(task)
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
school_students = [
	[  # это – первый класс
		{'first_name': 'Вася'},
		{'first_name': 'Вася'},
	],
	[  # это – второй класс
		{'first_name': 'Маша'},
		{'first_name': 'Маша'},
		{'first_name': 'Оля'},
	]
]

# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша


y=0
for x in school_students:
	sort_list=[]
	for z in x:
		sort_var=z.get('first_name')
		sort_list.append(sort_var)
	y=y+1
	count=Counter(sort_list).most_common(1)
	print("Самое распространенное имя среди учеников класса {}: {}".format(y,count[0][0]))


task="Задание 4"
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
print(task)
school = [
	{'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
	{'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
	'Маша': False,
	'Оля': False,
	'Олег': True,
	'Миша': True,
}

# Пример вывода:
# В классе 2a 2 девочки и 0 мальчика.
# В классе 3c 0 девочки и 2 мальчика.

count_gender=[]
for x in school:
	female=0
	male=0
	class_num=x.get('class')
	class_students=x.get('students')
	for y in class_students:
		name=y.get('first_name')
		for z in is_male:
			if name==z:
				if is_male.get(z)==True:
					male=male+1
				else:
					female=female+1
	count_gender.append()
	print("В классе {} учатся {} мальчиков и {} девочек.".format(class_num, male, female))


task="Задание 5"
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков.
print(task)
school = [
	{'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
	{'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
	'Маша': False,
	'Оля': False,
	'Олег': True,
	'Миша': True,
}

# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

for x in school:
	female=0
	male=0
	class_num=x.get('class')
	class_students=x.get('students')
	for y in class_students:
		name=y.get('first_name')
		for z in is_male:
			if name==z:
				if is_male.get(z)==True:
					male=male+1
				else:
					female=female+1
	print("В классе {} учатся {} больше всего мальчиков и {} девочек.".format(class_num, male, female))

