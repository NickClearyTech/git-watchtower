# builder container
FROM python:3.10-slim AS builder
COPY . /src/
WORKDIR /src

# Install system updates, build dependencies, and build package
RUN apt-get update && \
  apt-get upgrade -y && \
  apt-get install -y \
    curl build-essential && \
  pip install --no-cache-dir --upgrade -r requirements.build && \
  pip install --user --no-cache-dir .
ENV PATH=/root/.local/bin:$PATH

# main container without build dependencies
FROM python:3.10-slim as app
COPY requirements.build .

# System updates
RUN apt-get update && \
  apt-get upgrade -y && \
  rm -rf /var/lib/apt/lists/*
RUN pip install --no-cache-dir --upgrade -r requirements.build
COPY --from=builder /root/.local /root/.local
ENV PATH=/root/.local/bin:$PATH
WORKDIR /root
ENTRYPOINT ["watchtower"]