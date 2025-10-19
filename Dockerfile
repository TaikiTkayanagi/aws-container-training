From ubuntu:25.04
RUN apt-get update && apt-get install -y python3-pip python3-venv curl unzip git


RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"\
    && unzip awscliv2.zip\
    && ./aws/install 

SHELL ["/bin/bash", "-c"]

RUN curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash

RUN . $HOME/.nvm/nvm.sh && nvm install 22.20.0
