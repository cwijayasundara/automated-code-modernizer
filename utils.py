import os


def safe_write(path, code):
    path = "./software/" + path
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w+') as f:
        f.write(code)


def create_project_dir(directory):
    if not os.path.exists(directory):
        print('Creating project directory ' + directory)
        os.makedirs(directory)
