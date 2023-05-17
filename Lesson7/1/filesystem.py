import os

# # Current directory
# current_dir = os.getcwd()
# print(f'My current working directory is: {current_dir}')
#
# # Change current directory
# os.chdir('..')
# new_current_dir = os.getcwd()
# print(f'My new working directory is: {new_current_dir}')

# Get all directories
content = list(os.scandir(os.getcwd()))
print(f'List of directories: {content}')

# # Check directory
# _, lecture_7_dir, lecture_8_dir = content
#
# if os.path.exists(lecture_7_dir.path):
#     print(f'The file path {lecture_7_dir.path} exists')
# else:
#     print(f'The file path {lecture_7_dir.path} does not exist')
#
# if os.path.isdir(lecture_7_dir.path):
#     print(f'The file path {lecture_7_dir.path} belongs to directory')
# else:
#     print(f'The file path {lecture_7_dir.path} does not belong to directory')

# # Get all from directory
# print('Show directory content')
# for root, dirs, files in os.walk(lecture_7_dir.path):
#     print(f'Current directory: {root}')
#
#     print('Show all files:')
#     for name in files:
#         print(os.path.join(root, name))
#
#     print('Show all directories:')
#     for name in dirs:
#         print(os.path.join(root, name))
#
# # Create directory
# new_dir = os.path.join(new_current_dir, 'Лекция 9')
# os.mkdir(new_dir)
# result = os.listdir(new_current_dir)
# print(result)
#
# # Delete directory
# os.rmdir(os.path.join(new_dir))
# result = os.listdir(new_current_dir)
# print(result)
