def is_that_jpg_file(bin_content):
    jpg_header = ('0xff', '0xd8', '0xff')

    for header, i in zip(jpg_header, range(len(jpg_header))):
        if header != hex(bin_content[i]):
            return False

    return True


with open('wallpaper.jpg', 'rb+') as file:
    content = file.read()

    if is_that_jpg_file(content):
        print("That's JPEG file!")
        filename, file_extension = file.name.split('.')
        new_filename = f'{filename}_copy.{file_extension}'

        with open(new_filename, 'wb') as new_file:
            new_file.write(content)
            print('File was copied')

    else:
        print("That's NOT JPEG file!")
