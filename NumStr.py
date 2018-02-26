#1
a = 2
b = 4.5
print(a + b)
#2
v = input('Введите число от 1 до 10: ')
print(int(v)*10)
#3
name = input('Введите ваше имя: ')
name2='Привет, {}, как дела?'.format(name)
print('Привет, '+name+', как дела?')
print(name2)
#4
float('1')  # 1.0
#int('2.5')  # ошибка
bool(1)  # True
bool('')  # False
bool(0)  # False
