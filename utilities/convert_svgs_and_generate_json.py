import os
import json

def convert_svgs_to_html(input_directory, output_directory, level):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    svg_files = sorted([f for f in os.listdir(input_directory) if f.endswith(".svg")])

    svg_paths = []

    for svg_file in svg_files:
        svg_path = os.path.join(input_directory, svg_file)

        with open(svg_path, "r", encoding="utf-8") as f:
            svg_content = f.read()

        title = os.path.splitext(svg_file)[0]
        anchor_id = title.replace(" ", "_")

        html_content = f'<a id="{anchor_id}">\n{svg_content}\n</a>\n'
        output_file = os.path.join(output_directory, f'{anchor_id}.html')

        with open(output_file, "w", encoding="utf-8") as out_svg:
            out_svg.write(html_content)

        svg_paths.append(f"./svg_html/{anchor_id}.html")

    return svg_paths


input_directories = {
    "Level1": "D:\CODE\TKA\Guide_Website\Level1Artboards",
    "Level2": "D:\CODE\TKA\Guide_Website\Level2Artboards"
}
output_directory = "D:\CODE\TKA\Guide_Website\svg_html"

all_svg_paths = []

for level, input_dir in input_directories.items():
    svg_paths = convert_svgs_to_html(input_dir, output_directory, level)
    all_svg_paths.extend(svg_paths)

output_file = os.path.join(os.path.dirname(output_directory), "svg_paths.json")
with open(output_file, "w", encoding="utf-8") as output:
    json.dump(all_svg_paths, output)

print("SVG paths generated successfully!")
