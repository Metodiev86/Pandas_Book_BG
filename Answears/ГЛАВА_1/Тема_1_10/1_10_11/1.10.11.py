#Създайте програма, която архивира (zip) дадена директория, включително всички нейни поддиректории и файлове, и записва архива в нов файл. Можете да използвате модула zipfile.

import os
import zipfile

def zip_directory(folder_path, output_zip):
    # Създаване на zip архив в режим 'w' (write) с компресия ZIP_DEFLATED
    with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        # os.walk преминава през всички файлове и поддиректории в дадената директория
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)  # Пълния път към файла
                # Запазване на относителния път, за да се поддържа структурата на директорията в архива
                arcname = os.path.relpath(file_path, folder_path)
                zipf.write(file_path, arcname)  # Записване на файла в архива с относителния път

    # Извеждаме съобщение, когато архивирането е успешно
    print(f"Директорията е архивирана успешно като '{output_zip}'")


