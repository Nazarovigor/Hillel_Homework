# File not found error
filename = 'hellow_world_non_exists.txt'
try:
    file = open(filename, 'r')
    file.close()

except FileNotFoundError:
    print(f'There is no file with that name: {filename}')

# Read error
filename = 'wallpaper.jpg'
try:
    file = open(filename, 'r')
    file.readlines()
    file.close()

except UnicodeDecodeError:
    print(f'This file cannot be read as text: {filename}')


# Regular way to handle file error
filename = 'hellow_world.txt'
try:
    file = open(filename, 'r')
    first_5_symbols = file.read(5)
    print(f'First 5 symbols from file: {first_5_symbols}')
    file.close()

except (OSError, IOError) as e:
    print(f'Unexpected error found during work with: {filename}\nError: {e}')
