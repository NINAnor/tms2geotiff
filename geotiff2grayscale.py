#!/usr/bin/env python3

from osgeo import gdal

import argparse


def grayscale(input_path, output_path):
    src = gdal.Open(input_path, gdal.gdalconst.GA_Update)
    driver = gdal.GetDriverByName('GTiff')
    dst = driver.CreateCopy(output_path, src, 1)

    colors = gdal.ColorTable()
    colors.CreateColorRamp(0, (0, 0, 0), 255, (255, 255, 255))

    band = dst.GetRasterBand(1)
    band.SetRasterColorTable(colors)
    band.SetRasterColorInterpretation(gdal.GCI_PaletteIndex)
    del src


def main():
    parser = argparse.ArgumentParser(description="Convert GeoTIFFs with palette to grayscale")
    parser.add_argument("input")
    parser.add_argument("output")
    args = parser.parse_args()
    grayscale(args.input, args.output)


if __name__ == "__main__":
    main()
