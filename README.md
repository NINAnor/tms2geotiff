tms2geotiff fetches the smallest tile (from a TMS resource) which includes the specified bounding box, and generates a GeoTIFF file.

# Dependencies

- Python
  - mercantile
  - gdal
  - requests

# Usage (using Docker)

```bash
docker build -t tms2geotiff .
docker run --rm -v $PWD:/host --workdir /host tms2geotiff $LON_MIN $LAT_MIN $LON_MAX $LAT_MAX "$URL"
```
