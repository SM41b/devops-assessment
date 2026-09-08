FROM jenkins/jenkins:lts-jdk17

USER root

RUN apt-get update \
    && apt-get install -y docker.io curl python3 python3-pip \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install --break-system-packages fastapi uvicorn pytest httpx
