import pickle
import json

some_dict = {'a': 1, 'b': 2}

# Serialize variable to file
dump_str = pickle.dumps(some_dict)
with open('variable.txt', 'wb') as file:
    file.write(dump_str)

# Deserialize variable from file
with open('variable.txt', 'rb') as file:
    content = file.read()

new_dict = pickle.loads(content)
print(some_dict == new_dict)


# Serialize variable to file
dump_str = json.dumps(some_dict)
with open('variable.txt', 'w') as file:
    file.write(dump_str)

# # Deserialize variable from file
# with open('variable.txt', 'r') as file:
#     content = file.read()
#
# new_dict = json.loads(content)
# print(some_dict == new_dict)
