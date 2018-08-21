#!/bin/sh
apt-get install -y \
        cmake \
        libgtk2.0-dev \
        libavcodec-dev \
        libavformat-dev \
        libswscale-dev \
        && \
    mkdir /home/root/opencv && \
    cd /home/root/opencv && \
    wget https://github.com/Itseez/opencv/archive/3.3.0.zip && \
    unzip 3.3.0.zip && \
    cd opencv-3.3.0 && \
    mkdir build && \
    cd build && \
    cmake -D CMAKE_BUILD_TYPE=Release -D CMAKE_INSTALL_PREFIX=/usr/local -D WITH_IPP=ON .. && \
    make -j7 && \
    make install

