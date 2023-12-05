import os

folder_path = r"D:\CODE\TKA\Guide_Website\Level1Artboards"
output_file = "filenames.txt"
encoding = "utf-8"

with open(output_file, "w", encoding=encoding) as file:
    for filename in os.listdir(folder_path):
        file.write(filename + "\n")
