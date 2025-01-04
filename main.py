import os
from md_header import write_github_page_header
from pathlib import Path

def get_directory_md_paths():
    directory = os.environ.get("MD_FILES_ROOT_DIRECTORY")
    return list(Path(directory).rglob('*.md'))

def write_header_on_file(file_path):
    file = Path(file_path)
    content = file.read_text()
    title = write_github_page_header(content)
    file.write_text(title+"\n"+content)

def main():
    files = get_directory_md_paths()
    for file in files:
        write_header_on_file(file)

if __name__ == "__main__":
    main()