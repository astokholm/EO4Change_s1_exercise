#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    30574 Earth observations for monitoring changes (EO4Change) Day 3 exercise with Sentinel-1 SAR
    Download Sentinel-1 SAR image.
"""

# -- File info -- #
__author__ = ['Andreas R. Stokholm']
__copyright__ = ['A. Stokholm']
__contact__ = ['stokholm@space.dtu.dk']
__version__ = '0.0.1'
__date__ = '2022-06-06'

# -- Built-in modules -- #
import os

# -- Third-party modules -- #
from sentinelsat.sentinel import SentinelAPI, read_geojson, geojson_to_wkt

# -- Proprietary modules -- #


# -- Read here -- #
# In this part of the exercise, you should only change entries in the dictionary below and run the whole script,
# e.g. either by using run file, or doing 'python s1_get.py' in the command line while being in the correct directory.
# Add the start and end date of your search, and the footprint_file. There should already be a geojson file but
# feel free to make a new one. :)

SENTINELSAT_OPTIONS = {
    'date': [, ],  # Start, End date, YYYYMMDD
    'footprint_file': '',  # name of geojson file. Inset relevant filename or make your own https://geojson.io
    'platformname': 'Sentinel-1',  # Satellite platform name, e.g. Sentinel-1, 2
    'producttype': 'GRD',  # find satellite products at https://sentinel.esa.int/web/sentinel/user-guides/
    'sensoroperationalmode': 'IW',  # Acquisition mode
    'processingmode': 'Offline',  # Processing mode, i.e. Offline, NRT
    'username': 'eo4change',  # Signup @ https://scihub.copernicus.eu/dhus/#/self-registration
    'password': 'eo4change!',
    'data_dir': 's1_data',  # Directory to download data to.
    'download_index': 1,  # Must be > 1.
}


def main(sentinelsat_options: dict):
    # Make data directory (if it does not exist).
    os.makedirs(os.path.join(os.getcwd(), sentinelsat_options['data_dir']), exist_ok=True)

    # Initialize API.
    api = SentinelAPI(sentinelsat_options['username'], sentinelsat_options['password'],
                      'https://scihub.copernicus.eu/dhus/')
    # Get geojson footprint.
    footprint = geojson_to_wkt(read_geojson(sentinelsat_options['footprint_file']))

    # Find matching files based on criteria.
    products = api.query(area=footprint,
                         date=sentinelsat_options['date'],
                         platformname=sentinelsat_options['platformname'],
                         producttype=sentinelsat_options['producttype'],
                         )

    # convert to Pandas DataFrame
    products_df = api.to_dataframe(products)

    if len(products_df) < 1:
        exit('No products available.')

    print(f"Number of products available: {len(products_df)}")
    print(f"Downloading product: {products_df.head(sentinelsat_options['download_index'])['title']}")

    # Select and download product to data directory.
    product_df = products_df.head(sentinelsat_options['download_index'])  # Get desired product based on selected index.
    cwd = os.getcwd()  # remember current work directory (CWD).
    os.chdir(sentinelsat_options['data_dir'])  # Change directory.
    api.download_all(product_df.index)  # Download product. Needs '.index' as it cannot download df directly.
    os.chdir(cwd)  # Return to project directory.


if __name__ == '__main__':
    main(sentinelsat_options=SENTINELSAT_OPTIONS)
