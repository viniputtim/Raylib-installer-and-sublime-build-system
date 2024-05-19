#!/bin/bash

# Atualize os pacotes
sudo apt update

# Instale as dependências
sudo apt install -y build-essential git cmake libasound2-dev libx11-dev libxrandr-dev libxi-dev \
libgl1-mesa-dev libglu1-mesa-dev libglfw3 libglfw3-dev libxcursor-dev libxinerama-dev libwayland-dev \
libxkbcommon-dev

# Clone o repositório raylib
git clone https://github.com/raysan5/raylib.git raylib

# Navegue para o diretório raylib
cd raylib

# Crie um diretório de construção e navegue até ele
mkdir build && cd build

# Configure o projeto com opção BUILD_SHARED_LIBS ativada
cmake -DBUILD_SHARED_LIBS=ON ..

# Compile o projeto
make

# Instale os arquivos compilados
sudo make install

# Atualize as configurações de linker
sudo ldconfig
