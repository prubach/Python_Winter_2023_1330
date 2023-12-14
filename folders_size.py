import os
import shutil

my_folder = 'venv'

print(os.listdir(my_folder))
for f in os.listdir(my_folder):
    is_file = os.path.isfile(os.path.join(my_folder, f))
    print(f'{f}: {is_file}')

#os.makedirs()
#os.remove()

#TODO - given a folder please sum up the space occupied by all regular files in it