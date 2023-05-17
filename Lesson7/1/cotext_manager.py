with open('hellow_world.txt', 'w') as file:
    hello_list = [f'My {i} Hello World!\n' for i in range(10)]
    file.writelines(hello_list)
