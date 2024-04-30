import sys
import os

sys.path.append("..")


def delete_files_in_output():
    output_folder_path_list = ['images/output', 'video/output']

    for folder in output_folder_path_list:
        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)
            try:
                if os.path.isfile(file_path):
                    os.remove(file_path)
            except Exception as e:
                print(f'Ошибка при удалении файла {file_path}. {e}')
