ARG DOCKER_VERISON=20-dind
FROM docker:${DOCKER_VERISON}

WORKDIR /usr/ahu/code/
COPY ./ dind/

WORKDIR /usr/ahu/code/dind
ENTRYPOINT ["sh", "./start.sh"]
EXPOSE 2375