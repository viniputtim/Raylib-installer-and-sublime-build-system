import os, sys

if not os.path.exists(os.path.join('..', 'bin')):
    os.mkdir(os.path.join('..', 'bin'))

file_name = sys.argv[1]
executable = f'{os.path.join('..', 'bin', os.path.splitext(sys.argv[1])[0])}.out'
file_path = sys.argv[2]
library = sys.argv[3] if len(sys.argv) == 4 else ''
cpp_files = ''
include_folder = 'include'
flags = ''

if library == 'raylib':
    flags = '-lraylib -lglfw -lGL -lm -lpthread -ldl -lrt -lX11'


for root, folders, files in os.walk(file_path):
    for file in files:
        cpp_files = f'{cpp_files} {os.path.join(root, file)}' if file.endswith('.cpp') else cpp_files

cmd = f'g++ {cpp_files} -o {executable} -I {include_folder} {flags}'

print(cmd)
os.system(cmd)
os.system(executable)
