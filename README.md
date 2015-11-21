# SMOS

Tools for processing data from the [Soil Moisture and Ocean Salinity (SMOS)](http://www.esa.int/Our_Activities/Observing_the_Earth/SMOS/Introducing_SMOS) satellite.

1. Downloads from their FTP server
2. Converts to netcdf then to shapefile (yes, the satellite data is vector points)
3. Rasterizes the data using inverse distance weighting
4. Upload to mapbox (TBD)

## Access rights

You've got to apply for FTP access. Sorry

After you've got that taken care of, you need to set two environment variables:

    SMOS_USERNAME=mperry
    SMOS_PASSWORD=secretz

## Download the SMOS conversion tool

This is a critical piece to the toolkit. It's free but the license not specified. It's assumed to be public domain but to be safe you've got to grab your own copy

    wget http://org.esa.s3tbx.s3.amazonaws.com/software/installers/v1.0.1/smos-ee-to-netcdf-standalone.zip
    unzip smos-ee-to-netcdf-standalone.zip

SMOS NetCDF Conversion Tool docs
https://earth.esa.int/documents/10174/479378/SMOS-BOX-Format_Conversion_User_Guide

## TODO

* Land/Sea Mask
* Weekly or most recent
* Ocean Salinity
* Color ramp
* Contouring
* merging and compositing
* Uploading
