# -*- coding: utf-8 -*-
"""
@Time          : 2024/12/18 00:00
@Author        : Shinhye Han
@File          : utils.py
@Noice         : 
@Description   : Utility functions including handling TIFF or jason files.
@How to use    : Import functions like load_tiff and save_json.

@Modificattion :
    @Author    :
    @Time      :
    @Detail    :
"""

from typing import Tuple
import numpy as np
from osgeo import gdal
import json


def load_tiff(file_path: str) -> Tuple[np.ndarray, dict]:
    """
    Load a TIFF file and return the raster data and metadata.

    Args:
        file_path (str): Path to the TIFF file.

    Returns:
        Tuple[np.ndarray, dict]: Raster data as a NumPy array and metadata as a dictionary.
    """
    dataset = gdal.Open(file_path)
    if dataset is None:
        raise FileNotFoundError(f"Unable to open file: {file_path}")

    band = dataset.GetRasterBand(1)
    array = band.ReadAsArray()
    metadata = {
        "geo_transform": dataset.GetGeoTransform(),
        "projection": dataset.GetProjection(),
        "size": (dataset.RasterXSize, dataset.RasterYSize)
    }

    return array, metadata


def save_tiff(file_path: str, array: np.ndarray, geo_transform: Tuple, projection: str) -> None:
    """
    Save a NumPy array as a TIFF file with the given geospatial information.

    Args:
        file_path (str): Path to save the TIFF file.
        array (np.ndarray): Data to save.
        geo_transform (tuple): Geospatial transformation.
        projection (str): Projection information.
    """
    driver = gdal.GetDriverByName("GTiff")
    out_raster = driver.Create(file_path, array.shape[1], array.shape[0], 1, gdal.GDT_Float32)
    if out_raster is None:
        raise IOError(f"Failed to create file: {file_path}")

    out_raster.SetGeoTransform(geo_transform)
    out_raster.SetProjection(projection)
    out_band = out_raster.GetRasterBand(1)
    out_band.WriteArray(array)
    out_band.FlushCache()


def load_json(file_path: str) -> dict:
    """
    Load a JSON file.

    Args:
        file_path (str): Path to the JSON file.

    Returns:
        dict: Parsed JSON content.
    """
    with open(file_path, "r") as f:
        return json.load(f)


def save_json(file_path: str, data: dict) -> None:
    """
    Save a dictionary to a JSON file.

    Args:
        file_path (str): Path to the JSON file.
        data (dict): Data to save.
    """
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)
