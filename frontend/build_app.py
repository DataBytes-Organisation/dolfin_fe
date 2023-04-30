import os
import shutil
from zipfile import ZipFile
from datetime import datetime

now = datetime.now().isoformat()
now = now.replace('-', '_')
now = now.replace(':', '_')
folder_name = now.replace('.', '_')

# create a folder in build dir


mode = 0o666
try:
    build_location = os.path.join(os.getcwd(), 'build')
    os.mkdir(build_location, mode)
except FileExistsError:
    print("Did not create Build Folder, already Exists")

folder_location = os.path.join(os.getcwd(), 'build', folder_name)
os.mkdir(folder_location, mode)
print("Created Build Instance folder successfully")

# copy folders to build dir
to_copy = ['.ebextensions', 'assets', 'classes', 'components', 'data', 
            'environment', 'layout', 'pages', 'utils', 'app.py', 'application.py', 'requirements.txt']

for file in to_copy:
    src = os.path.join(os.getcwd(), file)
    dest = os.path.join(folder_location, file)
    if ('.py' in src) or ('.txt' in src):
        shutil.copyfile(src, dest)
    else:
        shutil.copytree(src, dest)

# create .zip in build dir
print(folder_location)
shutil.make_archive('app', 'zip', folder_location)