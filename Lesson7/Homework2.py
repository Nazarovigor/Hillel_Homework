# Написать скрипт, который подсчитает количество папок и файлов по заданному пути.
# Если такого нет, то по всей системе(/ - для линукс/мак. Диск С - для виндоус).
# Для удобства можно установить граничное значение числа папок(и/или файлов),
# после которого скрипт не будет продолжать работу.
# Среди найденных файлов показать самый большой и самый маленький по размеру, а так же с самым длинным и коротким именем.
# Если во время работы скрипт был прерван(KeyboardInterrupt), то промежуточные результаты сериализуются в файл
# и при повторном запуске эти пути исключаются из проверки.
import os
import pickle


def input_file():
    try:
        file = input('Please enter a filename: ')
        if os.path.exists(file):
            return file
        else:
            print(f'There is no any {file}, I return "C:\\"')
            file = 'C:\\'
            return file

    except KeyboardInterrupt:
        return 'You interrupt the program, try again.'


# функция для подсчета количества папок и файлов
def count_items(path, max_items, checkpoint_file=None):
    count = {'dirs': 0, 'files': 0}
    largest_file = {'name': None, 'size': 0}
    smallest_file = {'name': None, 'size': float('inf')}
    longest_name = {'name': None, 'length': 0}
    shortest_name = {'name': None, 'length': float('inf')}
    checked_paths = set()

    # если есть сохраненный прогресс, загружаем его
    if checkpoint_file and os.path.exists(checkpoint_file):
        with open(checkpoint_file, 'rb') as f:
            checked_paths = pickle.load(f)

    # проходим по всем элементам в заданной директории
    for root, dirs, files in os.walk(path):
        for d in dirs:
            dir_path = os.path.join(root, d)
            if dir_path not in checked_paths:
                count['dirs'] += 1
                checked_paths.add(dir_path)
                if count['dirs'] + count['files'] >= max_items:
                    return count, largest_file, smallest_file, longest_name, shortest_name, checked_paths

        for f in files:
            file_path = os.path.join(root, f)
            if file_path not in checked_paths:
                count['files'] += 1
                checked_paths.add(file_path)
                try:
                    file_size = os.path.getsize(file_path)
                    if file_size > largest_file['size']:
                        largest_file['size'] = file_size
                        largest_file['name'] = file_path
                    if file_size < smallest_file['size']:
                        smallest_file['size'] = file_size
                        smallest_file['name'] = file_path
                except OSError:
                    pass
                if len(f) > longest_name['length']:
                    longest_name['length'] = len(f)
                    longest_name['name'] = file_path
                if len(f) < shortest_name['length']:
                    shortest_name['length'] = len(f)
                    shortest_name['name'] = file_path
                if count['dirs'] + count['files'] >= max_items:
                    return count, largest_file, smallest_file, longest_name, shortest_name, checked_paths

        # сохраняем результаты после обработки каждой папки, чтобы не потерять прогресс при возникновении ошибки
        if checkpoint_file:
            with open(checkpoint_file, 'wb') as f:
                pickle.dump(checked_paths, f)

    return count, largest_file, smallest_file, longest_name, shortest_name, checked_paths

# граничное значение числа папок и файлов
max_items = 100000

# имя файла для сохранения результатов промежуточной работы
checkpoint_file = 'checkpoint.pkl'


try:
    path = input_file()
    count, largest_file, smallest_file, longest_name, shortest_name, checked_paths = count_items(path, max_items)
    print(f'Number of directories: {count}')
    print(f'Largest file: {largest_file}')
    print(f'Smallest file {smallest_file}')
    print(f'Longest name: {longest_name}')
    print(f'Shortest name: {shortest_name}')
except KeyboardInterrupt:
    print('Keyboard interrupt, please try again')



