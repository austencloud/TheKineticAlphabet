import os
import chardet
import codecs

input_directory = "D:\CODE\TKA\Guide_Website\Level1Artboards"
output_directory = "D:\CODE\TKA\Guide_Website\svg_html"

if not os.path.exists(output_directory):
    os.makedirs(output_directory)

svg_files = sorted([f for f in os.listdir(input_directory) if f.endswith(".svg")])

for svg_file in svg_files:
    svg_path = os.path.join(input_directory, svg_file)
    
    # Determine the character encoding of the SVG file
    with open(svg_path, 'rb') as f:
        result = chardet.detect(f.read())
        encoding = result['encoding']

    try:
        with codecs.open(svg_path, "r", encoding=encoding) as f:
            svg_content = f.read()

        title = os.path.splitext(svg_file)[0]
        anchor_id = title.replace(" ", "_")

        html_content = f'<a id="{anchor_id}">\n{svg_content}\n</a>\n'
        output_file = os.path.join(output_directory, f'{anchor_id}.html')

        with codecs.open(output_file, "w", encoding="utf-8") as out_f:
            out_f.write(html_content)

    except UnicodeEncodeError as e:
        print(f"Encoding issue with {svg_file}: {e}")
