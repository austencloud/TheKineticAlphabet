import os
import shutil
import re

def create_folders_from_images(source_folder):
    if not os.path.exists(source_folder):
        print(f"Source folder not found: {source_folder}")
        return

    for filename in os.listdir(source_folder):
        file_path = os.path.join(source_folder, filename)
        
        if os.path.isfile(file_path) and (filename.endswith('.png') or filename.endswith('.jpg') or filename.endswith('.jpeg')):
            # Remove the file extension to get the folder name
            folder_name = os.path.splitext(filename)[0]
            
            # Remove underscores, parentheses, and their contents
            folder_name = re.sub(r'_|\(.*?\)', '', folder_name)

            folder_path = os.path.join(source_folder, folder_name)
            
            # Create the folder if it doesn't exist
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            
            # Move the image into the newly created folder
            shutil.move(file_path, os.path.join(folder_path, filename))

# Usage example
source_folder = 'D:\The Kinetic Alphabet Repository Clone\SEQUENCES\Austen Cloud\Level 1 - Turns'
create_folders_from_images(source_folder)
