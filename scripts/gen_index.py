import sys
import getopt
import os
import pathlib
from shutil import copyfile

from jinja2 import Template

USAGE = """
Usage:
   gen_index.py -i|--input <input-folder> -o|--output <output-folder>"
"""


def walk_dir(path, ext=None):
    flat_files = []
    for root, dirs, files in os.walk(path, topdown=True):
        # Exclude hidden files
        files = [f for f in files if not f[0] == '.']
        dirs[:] = [d for d in dirs if not d[0] == '.']
        for f in files:
            if ext and not f.endswith(ext):
                continue
            flat_files.append(os.path.join(root, f))
    return flat_files


def main(argv):
    if len(argv) != 4:
        print(USAGE)
        sys.exit(2)
    input_folder = None
    output_folder = None
    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["input=", "output="])
    except getopt.GetoptError:
        print(USAGE)
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print(USAGE)
            sys.exit()
        elif opt in ("-i", "--input"):
            input_folder = arg
        elif opt in ("-o", "--output"):
            output_folder = arg
    # Check check
    if not pathlib.Path(input_folder).is_dir() or not pathlib.Path(input_folder).exists():
        print('Input folder must be existed')
        sys.exit(2)
    if not pathlib.Path(output_folder).is_dir() or not pathlib.Path(output_folder).exists():
        print('Output folder must be existed')
        sys.exit(2)

    input_folder = os.path.abspath(input_folder)
    parent_input_folder = str(pathlib.Path(
        input_folder).parent.absolute()) + '/'
    output_folder = os.path.abspath(output_folder)

    # Walk through input folder
    flat_files = []
    for root, dirs, files in os.walk(input_folder, topdown=True):
        # Exclude hidden files
        files = [f for f in files if not f[0] == '.']
        dirs[:] = [d for d in dirs if not d[0] == '.']
        for f in files:
            if not f.endswith('.md'):
                continue
            new_file_name = os.path.join(
                root.replace(parent_input_folder, ''), f).replace('/', '-')
            flat_files.append(new_file_name.strip('.md'))
            src = os.path.join(root, f)
            dest = os.path.join(output_folder, new_file_name)
            copyfile(src, dest)
    # Generate the main page
    about_template = Template(
        open(f'{pathlib.Path.cwd()}/about.md.j2', 'r').read())
    with open(f'{output_folder}/about.md', 'w') as f:
        f.write(about_template.render(files=flat_files))


if __name__ == "__main__":
    main(sys.argv[1:])
