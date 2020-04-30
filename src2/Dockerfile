FROM ubuntu:18.04
MAINTAINER web@kujirahand.com

ENV DEBIAN_FRONTEND=noninteractive
ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP.UTF-8
ENV LC_ALL ja_JP.UTF-8

# install for Python
RUN set -x && \
    apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        curl \
        libfreetype6-dev \
        libpng-dev \
        libzmq3-dev \
        pkg-config \
        python3 \
        python3-dev \
        python3-pip \
        python3-setuptools \
        python3-wheel \
        gcc \
        git \
        rsync \
        software-properties-common \
        libgtk2.0-dev \
        libavcodec-dev \
        libavformat-dev \
        libswscale-dev \
        libopencv-dev \
        libdc1394-22 \
        libdc1394-22-dev \
        libjpeg-dev \
        libtiff5-dev \
        libavcodec-dev \
        libavformat-dev \
        libswscale-dev \
        libxine2-dev \
        libv4l-dev \
        libtbb-dev \
        libqt4-dev \
        libfaac-dev \
        libmp3lame-dev \
        libopencore-amrnb-dev \
        libopencore-amrwb-dev \
        libtheora-dev \
        libvorbis-dev \
        libxvidcore-dev \
        # libjasper-dev \
        # libgstreamer0.10-dev \
        # libgstreamer-plugins-base0.10-dev \
        x264 \
        v4l-utils \
        unzip \
        nano \
        language-pack-ja \
        fonts-ipafont \
        && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# update pip
RUN set -x && \
    pip3 install --upgrade pip

# install library
RUN set -x && \
    pip3 install \
        requests \
        setuptools \
        Pillow \
        nose \
        h5py \
        ipykernel \
        jupyter \
        matplotlib \
        mlxtend \
        numpy \
        pandas \
        scipy \
        scikit-learn==0.22.2 \
        seaborn \
        opencv-python==4.1.0.25 \
        tensorflow==2.1.0 \
        keras==2.3.1 \
        flask==1.1.1

RUN set -x && \
    mkdir -p /root/.config/matplotlib && \
    echo 'backend : Agg' > /root/.config/matplotlib/matplotlibrc && \
    echo 'font.family : IPAPGothic' >> /root/.config/matplotlib/matplotlibrc





