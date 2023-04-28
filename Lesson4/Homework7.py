# Напишіть програму, яка виводить словник, в якому ключі є числами від 1 до 15 (обидва включені),
# а значення є квадратами ключів. Генерація ключів та значень має бути виконана через цикл.

#Variant1
#print(dict(zip(list(range(1,16)), list(x**2 for x in range(1,16)))))

#Variant2
keys = []
for i in range(1, 16):
    keys.append(i)

values = []
for j in range(1, 16):
    values.append(j**2)

print(dict(zip(keys, values)))

