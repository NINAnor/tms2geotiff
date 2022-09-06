#!/usr/bin/env python3

import mercantile
from osgeo import gdal
import requests

import argparse
import tempfile


def generate(url, output, *bbox):
    tile = mercantile.bounding_tile(*bbox)
    x, y, z = tile
    bbox = mercantile.bounds(tile)

    url = url.replace("{switch:a,b,c}", "a")  # Strava Heatmap workaround
    url = url.format(x=x, y=y, z=z, zoom=z)

    with tempfile.NamedTemporaryFile() as tiff:
        tiff.write(requests.get(url).content)
        gdal.Translate(
            f"tile-{z}-{x}-{y}.tiff",
            tiff.name,
            options=f"-a_srs EPSG:4326 -a_ullr {bbox.west} {bbox.north} {bbox.east} {bbox.south}",
        )


def main():
    parser = argparse.ArgumentParser(description="Generate GeoTIFFs from TMS tiles")
    parser.add_argument("minx", type=float)
    parser.add_argument("miny", type=float)
    parser.add_argument("maxx", type=float)
    parser.add_argument("maxy", type=float)
    parser.add_argument("url")
    args = parser.parse_args()
    generate(args.url, "test.geotiff", args.minx, args.miny, args.maxx, args.maxy)


if __name__ == "__main__":
    main()
