FROM archlinux/base

RUN pacman -Syu --noconfirm --needed \
    python \
    python-pip

ADD src /src

WORKDIR /src
RUN python setup.py install

WORKDIR /workdir

