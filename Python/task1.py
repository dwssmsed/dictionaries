# завдання 1
a = 60
b = 60
print(f'{a}*{b}={a*b}')
# завдання 2
seconds_per_hour = 3600
# завдання 3
c = 24
print(f'{c}*{seconds_per_hour}={c*seconds_per_hour}')
# завдання 4
seconds_per_day = 86400
# завдання 5
A = seconds_per_day/seconds_per_hour
print(A)
# завдання 6
B = seconds_per_day//seconds_per_hour
print(B)
# завдання 7
print(10+2)
print(14-2)
print(4*3)
print(24//2)
# завдання 8
my_number = 18
print(my_number)
# завдання 9
name = 'Mr David'
print(name.upper())
print(name.lower())
print(name.swapcase())

# задача 1
language = 'I had a cup of tea today'
print(language.replace('tea', 'coffee'))
# задача 2
Name = 'Sasha'
print(f'Hi, {Name}, how are you?')
# задача 3
famous_person = 'Albert Einstein'
message = f'{famous_person} once said, "A person who never made a mistake never tried anything new."'
print(message)
# задача 4
username1 = "---John Green---"
print(username1.strip('-'))
print(username1.lstrip('-'))
print(username1.rstrip('-'))
# задача 5
print('Serhii Danylashchuk\nUkraine\nChernivtsi')
# задача 6
meters = 1
inches = 39.3700787
foot = 3.3333333333
miles = 0.00062137119609836
print('{0:.2f} {1:.2f} {2:.2f}'.format(inches, foot, miles))
# задача 7
holidays_days = 28
holidays_hours = 24*holidays_days
holidays_minutes = 60*holidays_hours
holidays_seconds = 60*holidays_minutes
print('{:<10} {:<10} {:<10}'.format(
    holidays_hours, holidays_minutes, holidays_seconds))
#задача 8 і 11 input
#температура на вулиці n градусів Цельсі
your_degrees = int(input("enter any number "))
c = your_degrees
f = your_degrees * 32 + 9/5
k = c + 273.15
formatc = format(c,"14,.2f")
print(formatc)
formatf = format(f,"14,.2f")
print(formatf)
formatk = format(k,"14,.2f")
print(formatk)
# задача 10

x1 = 39.9075000
x2 = 116.3972300
y1 = 50.4546600
y2 = 30.5238000
x11 = math.radians(x1)
x22 = math.radians(x2)
y11 = math.radians(y1)
y22 = math.radians(y2)

distance = 6371.032 * math.acos(math.sin(x11) * math.sin(x22) + math.cos(x11) * math.cos(x22) * math.cos(y11 - y22))
print(distance)  # km



