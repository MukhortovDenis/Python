import re

text = input("Введите текст для кодировки: ");


while(True):
    try:
        key = input("Введите кодовое слово кодировки:  ")
        break
    except:
        print("Невозможный ключ ")

alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
alphabet_two = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

cipher = ""
j = 0
for i in text:
    if re.search(r"[0-9]", i):
        cipher += i
    else:
        if i == " ":
            cipher += " "
        else:
            if re.search(r"[А-Я]", i):
                cipher += alphabet_two[(alphabet_two.index(i) + alphabet.index(key[j])) % 33]
            else:
                cipher += alphabet[(alphabet.index(i) + alphabet.index(key[j])) % 33]
            if j == len(key) - 1:
                j = 0
            else:
                j += 1

print("Шифр Виженера: " + cipher)