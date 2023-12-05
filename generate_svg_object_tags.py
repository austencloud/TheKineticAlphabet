import os

input_directory = "D:/CODE/TKA/Guide_Website/svg_html"
output_file = "D:/CODE/TKA/Guide_Website/svg_collection.html"

svg_html_files = sorted([f for f in os.listdir(input_directory) if f.endswith(".html")])

with open(output_file, "w", encoding="utf-8") as out_f:
    out_f.write("<!DOCTYPE html>\n<html lang='en'>\n<head>\n<meta charset='UTF-8'>\n<title>SVG Collection</title>\n</head>\n<body>\n")
    
    for svg_html_file in svg_html_files:
        svg_path = os.path.join(input_directory, svg_html_file)
        anchor_id = os.path.splitext(svg_html_file)[0].replace(" ", "_")
        out_f.write(f'<object id="{anchor_id}" type="text/html" data="{svg_path}"></object>\n')
        
    out_f.write("</body>\n</html>")
