text = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
x = 13
y = input('Введите слово: ')
res = ''
for z in y:
    res += text[(text.index(z) + x) % len(text)]
print('Шифр Цезаря: "' + res + '"')