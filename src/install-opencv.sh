#!/bin/sh
apt-get install -y \
        wget \
        cmake \
        libgtk2.0-dev \
        libavcodec-dev \
        libavformat-dev \
        libswscale-dev \
        && \
    mkdir -p /usr/local/src/opencv && \
    cd /usr/local/src/opencv && \
    wget https://github.com/Itseez/opencv/archive/4.1.1.zip && \
    unzip 4.1.1.zip && \
    cd opencv-4.1.1 && \
    mkdir build && \
    cd build && \
    cmake -D CMAKE_BUILD_TYPE=Release -D CMAKE_INSTALL_PREFIX=/usr/local -D WITH_IPP=ON .. && \
    make -j7 && \
    make install

