import glob
import sys

import fiona
from fiona.crs import from_epsg
from netCDF4 import Dataset
import numpy as np

def convert(target, outshp, kind):
    pts = {}
    for i, nc in enumerate(ncs):
        sys.stderr.write("({} of {}) - Reading {}\n".format(i, len(ncs), nc))
        sm = Dataset(nc)
        lats = sm.variables['Latitude'][:]
        longs = sm.variables['Longitude'][:]
        if kind == 'SM':
            datas = sm.variables['Soil_Moisture'][:]
        elif kind == 'OS':
            datas = sm.variables['SSS3'][:]

        for data in zip(lats, longs, datas):
            lat, lon, val = [np.asscalar(x) for x in data]

            # zero assumed nodata, skip
            if val == 0:
                continue

            # overwrite, i.e. take the latest non-zero point
            pts[(lon, lat)] = val

    sys.stderr.write("Converting to shapefile\n")

    # Open a collection for writing.
    with fiona.open(
            outshp, 'w',
            crs=from_epsg(4326),
            driver='ESRI Shapefile',
            schema={
                'geometry': 'Point',
                'properties': {
                    'soil_moist': 'float'}}
            ) as dest:

        for (lon, lat), moist in pts.items():
            geom = {
                'type': "Point",
                'coordinates': [lon, lat]}
            feature = {
                'type': "Feature",
                'geometry': geom,
                'properties': {
                    'soil_moist': moist}}
            dest.write(feature)


if __name__ == "__main__":
    ncs = glob.glob(sys.argv[1] + "/*.nc")
    outshp = sys.argv[2]
    kind = sys.argv[3]
    convert(ncs, outshp, kind)
