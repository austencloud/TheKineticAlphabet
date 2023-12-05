import os
import shutil
import re
import os
import shutil
import re



def create_folders_from_images(source_folder: str):
    if not os.path.exists(source_folder):
        print(f"Source folder not found: {source_folder}")
        return

    for filename in os.listdir(source_folder):
        file_path = os.path.join(source_folder, filename)

        if os.path.isfile(file_path) and (
            filename.endswith(".png")
            or filename.endswith(".jpg")
            or filename.endswith(".jpeg")
        ):
            folder_name = os.path.splitext(filename)[0]
            folder_name = re.sub(r"_|\(.*?\)", "", folder_name)
            folder_path = os.path.join(source_folder, folder_name)

            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

            shutil.move(file_path, os.path.join(folder_path, filename))


source_folder = (
    "D:\The Kinetic Alphabet Repository Clone\SEQUENCES\Austen Cloud\Level 1 - Turns"
)
create_folders_from_images(source_folder)
