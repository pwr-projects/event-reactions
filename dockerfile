FROM archlinux/base

RUN pacman -Syu --noconfirm --needed python python-pip

ADD src /src

# PYTHON SETTINGS
COPY pyreqs.txt requirements.txt
RUN pip3 install -r requirements.txt

WORKDIR /workdir

