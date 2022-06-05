#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    30574 Earth observations for monitoring changes (EO4Change) Day 3 exercise with Sentinel-1 SAR
    Unzip Sentinel-1 SAR file.
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
import zipfile

# -- Proprietary modules -- #


def unzip(sentinelsat_options: dict):
    # -- Unzips all files in data directory. -- #
    cwd = os.getcwd()
    os.chdir(sentinelsat_options['data_dir'])

    files = os.listdir()
    zip_files = [file for file in files if '.zip' in file]  # Find all .zip files.
    safe_files = [file for file in files if '.SAFE' in file]  # Find all .SAFe files.

    files_to_unzip = [file for file in zip_files if not
                      [file.split('.')[0] in safe_file for safe_file in safe_files]]  # Find .zip files not unzipped.

    # Unzip files.
    for file_to_unzip in files_to_unzip:
        to_unzip = zipfile.ZipFile(file_to_unzip, 'r')
        to_unzip.extractall()
        to_unzip.close()
    os.chdir(cwd)
