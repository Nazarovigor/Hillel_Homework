# Існує список з іменами ["john", "marta", "james", "amanda", "marianna"],
# перетворити рядок, щоб кожне ім'я явно починалися з великої літери.

# Variant1
my_name_list = ["john", "marta", "james", "amanda", "marianna"]
my_name_list1 = list(map(lambda x: x.capitalize(), my_name_list))
print(my_name_list1)

# Variant2
# my_name_list = ["john", "marta", "james", "amanda", "marianna"]
# my_name_list1 = []
# for name in my_name_list:
#     my_name_list1.append(name.capitalize())
# print(my_name_list1)
