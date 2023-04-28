#У вас є список змінних у форматі CamelCase ["FirstItem", "FriendsList", "MyTuple"] ,
# перетворити його у список змінних для Пайтона snace_case, "friends_list", "my_tuple"]

my_variable = ["FirstItem", "FriendsList", "MyTuple"]

def my_convertor(name):
    """Convert camelCase to snake_case"""
    result = []
    for i, c in enumerate(name):
        if c.isupper() and i > 0:
            result.append('_')
        result.append(c.lower())
    return ''.join(result)

my_python_variable = []

for variable in my_variable:
    my_python_variable.append(my_convertor(variable))

print(my_python_variable)