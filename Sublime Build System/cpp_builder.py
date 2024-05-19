import os, sys


include_folder = 'include'
file_name = sys.argv[1]
file_path = sys.argv[2]
library = sys.argv[3] if len(sys.argv) == 4 else ''
flags = ''
bin_folder = os.path.join('..', 'bin')
executable = f'{os.path.join(bin_folder, os.path.splitext(file_name)[0])}.out'
cpp_files = ''

for root, folders, files in os.walk(file_path):
    for file in files:
        cpp_files = f'{cpp_files} {os.path.join(root, file)}' if file.endswith('.cpp') else cpp_files

if library == 'raylib':
    flags = '-lraylib -lglfw -lGL -lm -lpthread -ldl -lrt -lX11'

if not os.path.exists(bin_folder):
    os.mkdir(bin_folder)

cmd = f'g++ {cpp_files} -o {executable} -I {include_folder} {flags}'

print(cmd)
os.system(cmd)
os.system(executable)
