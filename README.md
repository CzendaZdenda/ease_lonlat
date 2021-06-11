# ease_lonlat
[![Build Status](https://travis-ci.com/CzendaZdenda/ease_lonlat.svg?branch=main)](https://travis-ci.com/CzendaZdenda/ease_lonlat) 

Small package to convert given geographic coordinates (longitude, latitude) to EASE(2)-grid coordinates (col, row) and vice versa.

This code is inspired by the 'easeconv-0.3' software, the EASE-Grid map transformation utilities Developed and distributed by the National Snow & Ice Data Center (NSIDC), University of Colorado at Boulder. But instead of defining projections and grids "from a scratch", the pyproj library and definition of grids from [NSIDC](https://nsidc.org/ease/ease-grid-projection-gt) have been used.

---

## MOTIVATION
Get SMOS (CATDS, 25km, global projection) row and col coordinates corresponding to the pixel of EASE2 grid with given lon-lat coordinates.

---

## SUPPORTED GRIDS
'N' stands for North Polar (Lambert's equal-area, azimuthal), 'S' for South Polar (Lambert's equal-area, azimuthal) and 'G' for Global (cylindrical, equal-area) projection.
3125km means pixel size of 3.125 km, 625 means 6.25 km and 125 means 12.5 km.

  - EASE2_G1km
  - EASE2_G3km, EASE2_N3km, EASE2_S3km
  - EASE2_G3125km, EASE2_N3125km, EASE2_S3125km
  - EASE2_G625km, EASE2_N625km, EASE2_S625km
  - EASE2_G9km, EASE2_N9km, EASE2_S9km
  - EASE2_G125km, EASE2_N125km, EASE2_S125km
  - EASE_G125km, EASE_N125km, EASE_S125km
  - EASE2_G25km, EASE2_N25km, EASE2_S25km
  - EASE_G25km, EASE_N25km, EASE_S25km
  - EASE2_G36km, EASE2_N36km, EASE2_S36km

## TESTED GRIDS
Tested on SMAP data. EASE2-grids - 9km (N, S, G), 36km (N, G).

## NOT TESTED GRIDS
If you can test this code on some of the not tested grids, I would appreciate if you do it and let me know :) Especially EASE grids.

  - EASE-grids - all.
  - EASE2-grids - 1km, 3km, 3.125km, 6.25km and 25km

## USAGE

```python
from ease_lonlat import EASE2GRID, SUPPORTED_GRIDS

# define new grid by yourself
grid = EASE2GRID(name='EASE2_G36km', epsg=6933, x_min=-17367530.45, y_max=7314540.83, res=36032.22, n_cols=964, n_rows=406)

# or using parameters taken from NSIDC and kept in SUPPORTED_GRIDS
grid = EASE2GRID(name='EASE2_G36km', **SUPPORTED_GRIDS['EASE2_G36km'])

# convert longitude and latitude to row and col indices
point_lon = 17.4
point_lat = 49.4

# row should be 48, col should be 528
col, row = grid.lonlat2rc(lon=point_lon, lat=point_lat)

# get lon, lat of the center of the pixel
pixel_center_lon, pixel_center_lat = grid.rc2lonlat(col=col, row=row)
```
