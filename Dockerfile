FROM debian:11
WORKDIR /app

RUN --mount=type=cache,target=/var/cache/apt \
    --mount=type=cache,target=/var/lib/apt/lists \
    apt-get -q -y update && \
    DEBIAN_FRONTEND=noninteractive apt-get -yq install \
        python3-gdal \
        python3-mercantile \
        python3-requests \
        ``

COPY tms2geotiff.py .
ENTRYPOINT ["/usr/bin/env", "python3", "tms2geotiff.py"]
CMD ["--help"]
