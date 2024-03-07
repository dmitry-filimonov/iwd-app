import os
import glob

def rename_files_in_directory(directory, file_pattern, image_paths_file):
    '''
    Функция ищет файлы .jpg в указанной директории и переименовывает их
    по шаблону 'img_x.jpg'
    '''
    files = glob.glob(os.path.join(directory, file_pattern))
    counter = 1
    for file in files:
        try:
            new_file_name = os.path.join(directory, f'img_{counter}.jpg')
            os.rename(file, new_file_name)
            print(f"{file} has been renamed to {new_file_name}")
            
            # Update the image_paths file
            with open(image_paths_file, 'a') as f:
                f.write(f"{new_file_name}\n")
            
            counter += 1
        except FileNotFoundError:
            print(f"The file {file} does not exist.")
        except PermissionError:
            print(f"You do not have permission to rename {file}.")

# пример использования
directory = 'C:\\Users\\dmf2\\Documents\\GitHub\\iwd-app\content'
file_pattern = '*.jpg'
image_paths_file = 'C:\\Users\\dmf2\\Documents\\GitHub\\iwd-app\image_paths.txt'
rename_files_in_directory(directory, file_pattern, image_paths_file)


