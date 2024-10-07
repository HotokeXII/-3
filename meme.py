#ЛАБА №3
#1.открытие и чтение файла
#чтение всего файла
with open('example', 'r') as file:
    content = file.read()
print(content)

#построчное чтение
with open('example', 'r') as file:
    for line in file:
        print(line)

#2.запись в файл
file = open('user_input', 'w')
x = int(input('сколько фраз вы хотите добавить?: '))
for i in range(1, x+1):
    text = input('Введите текст: ')+' '
    file.write(text)
    print('записал')
file.close()

#3.запись в файл
try:
    with open('nofile', 'r') as file:
        content = file.read()
    print(content)
except FileNotFoundError:
    print('файл не найден')
