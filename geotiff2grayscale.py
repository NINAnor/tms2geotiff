#!/usr/bin/env python3

from osgeo import gdal

import argparse


def grayscale(path):
    colors = gdal.ColorTable()
    colors.CreateColorRamp(0, (0, 0, 0), 255, (255, 255, 255))

    src = gdal.Open(path, gdal.gdalconst.GA_Update)
    band = src.GetRasterBand(1)
    band.SetRasterColorTable(colors)
    band.SetRasterColorInterpretation(gdal.GCI_PaletteIndex)
    del src


def main():
    parser = argparse.ArgumentParser(description="Convert GeoTIFFs with palette to grayscale")
    parser.add_argument("path")
    args = parser.parse_args()
    grayscale(args.path)


if __name__ == "__main__":
    main()
