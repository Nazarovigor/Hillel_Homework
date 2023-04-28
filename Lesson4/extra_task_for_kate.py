# 1. У тебя есть лист например: 33, 2, 44, 2, 15, 34, 33
# 2. Тебе нужно превратить его в сет, чтоб избавиться от дубликатов
# 3. Вернуть список в том же порядке, как и был, но без дубликатов уже, то бишь: 33, 2, 44, 15, 34

my_list = [33, 33, 2, 15, 44, 2, 15, 34, 33, 44]

my_set = set(my_list)
result = []

for numb in my_set:
    for elem in my_list:
        if (elem in my_set) and (elem not in result):
            result.append(elem)

print(result)
