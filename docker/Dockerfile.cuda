FROM nvidia/cuda:11.2.2-cudnn8-devel-ubuntu20.04
SHELL ["/bin/bash", "-c"]
ENV DEBIAN_FRONTEND=noninteractive
WORKDIR /root/


ARG PYTHON_VERSION=3.9
RUN \
    apt update \
    && apt install -y \
    apt-utils \
    curl \
    git \
    make \
    software-properties-common \
    && add-apt-repository -y ppa:deadsnakes/ppa \
    && apt install -y \
    python${PYTHON_VERSION} \
    python3-pip \
    && ln -snf /usr/bin/python${PYTHON_VERSION} /usr/bin/python \
    && ln -snf /usr/bin/python /usr/bin/python3 \
    && curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python - \
    && echo 'source $HOME/.poetry/env' >> ~/.bashrc
