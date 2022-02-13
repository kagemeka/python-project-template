FROM ubuntu:20.04
SHELL ["/bin/bash", "-c"]
ENV DEBIAN_FRONTEND=noninteractive
ARG GECKO_VERSION=0.30.0
ARG PYTHON_VERSION=3.9
WORKDIR /root/

RUN \
    apt update \
    && apt install -y \
    software-properties-common \
    && add-apt-repository -y ppa:deadsnakes/ppa \
    && apt install -y python${PYTHON_VERSION} \
    && ln -snf /usr/bin/python${PYTHON_VERSION} /usr/bin/python \
    && ln -snf /usr/bin/python /usr/bin/python3 \
    && apt install -y python3-pip

RUN \
    apt update \
    && apt install -y \
    apt-utils \
    curl \
    wget \
    git \
    make \
    python3-dev \
    python3-tk \
    tesseract-ocr \
    fonts-noto-cjk \
    firefox \
    && curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python - \
    && echo 'source $HOME/.poetry/env' >> ~/.bashrc \
    && python3 -m pip install -U pip \
    && wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
    && apt install -y ./google-chrome-stable_current_amd64.deb \
    && rm google-chrome-stable_current_amd64.deb \
    && wget https://github.com/mozilla/geckodriver/releases/download/v${GECKO_VERSION}/geckodriver-v${GECKO_VERSION}-linux64.tar.gz \
    && tar -C /usr/bin/ -xvzf geckodriver*.tar.gz \
    && rm geckodriver* \
    && chmod +x /usr/bin/geckodriver
