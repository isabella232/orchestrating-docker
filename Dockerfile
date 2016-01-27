FROM ubuntu:14.04.3

ADD ./scripts/bootstrap /scripts/bootstrap
RUN apt-get update && apt-get install -y curl && \
    /scripts/bootstrap
