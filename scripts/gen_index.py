import os
import pathlib
import sys

from jinja2 import Template

USAGE = "gen_index.py <folder>"


def main(argv):
    if len(argv) != 1:
        print(USAGE)
        sys.exit(2)

    folder = argv[0]
    if not pathlib.Path(folder).is_dir() or not pathlib.Path(folder).exists():
        print('Folder must be existed')
        sys.exit(2)
    folder_path = os.path.abspath(folder)

    # Walk through input folder
    _, _, files = next(os.walk(folder_path))
    files = [f.rstrip(".md")
             for f in files if not f.endswith('.md') or not f == "about.md"]
    # Generate the main page
    about_template = Template(
        open(f'{os.path.dirname(os.path.realpath(__file__))}/about.md.j2', 'r').read())
    with open(f'{folder_path}/about.md', 'w') as f:
        f.write(about_template.render(files=files))


if __name__ == "__main__":
    main(sys.argv[1:])
