import os
import glob

def rename_files_in_directory(directory, file_pattern):
    '''
    Функция ищет файлы .jpg в указанной директории и переименовывает их
    по шаблону 'img_x.jpg'
    '''
    files = glob.glob(os.path.join(directory, file_pattern = '*.jpg'))
    counter = 1
    for file in files:
        try:
            new_file_name = os.path.join(directory, f'img_{counter}.jpg')
            os.rename(file, new_file_name)
            print(f"{file} has been renamed to {new_file_name}")
            counter += 1
        except FileNotFoundError:
            print(f"The file {file} does not exist.")
        except PermissionError:
            print(f"You do not have permission to rename {file}.")

# пример использования
directory = '\path\to\files\img.txt'
file_pattern = '*.jpg'
rename_files_in_directory(directory, file_pattern)






