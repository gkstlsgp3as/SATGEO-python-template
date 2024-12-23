import os
import random
import numpy as np
import cv2
from osgeo import gdal, ogr
from tifffile import imwrite
from scipy.interpolate import interp1d
from PIL import Image
import pandas as pd
import yaml

# Function to create a land mask from a GeoTIFF file.
def create_land_mask(tif_name: str) -> np.ndarray:
    """
    Create a land mask using a vector layer and rasterize it to match the input GeoTIFF.

    Args:
        tif_name (str): Path to the input GeoTIFF file.

    Returns:
        np.ndarray: Rasterized land mask as a NumPy array.
    """
    ras_ds = gdal.Open(tif_name, gdal.GA_ReadOnly)
    gt = ras_ds.GetGeoTransform()

    # Define paths for vector data and temporary raster file
    vec_path = "/path/to/landmask/"
    vec_ds = ogr.Open(vec_path)
    lyr = vec_ds.GetLayer()

    temp_file = '/path/to/temporary/tiff/file'
    drv_tiff = gdal.GetDriverByName("GTiff")
    chn_ras_ds = drv_tiff.Create(temp_file, ras_ds.RasterXSize, ras_ds.RasterYSize, 1, gdal.GDT_Float32)
    chn_ras_ds.SetGeoTransform(gt)

    # Rasterize vector layer
    gdal.RasterizeLayer(chn_ras_ds, [1], lyr)
    chn_ras_ds.GetRasterBand(1).SetNoDataValue(0.0)
    chn_ras_ds = None

    # Read rasterized data
    raster = gdal.Open(temp_file)
    band_data = np.array(raster.GetRasterBand(1).ReadAsArray())
    return np.array(band_data, np.float32)


# Function to read GeoTIFF metadata and dimensions.
def read_geotiff_metadata(tif_name: str) -> Tuple[np.ndarray, int, int]:
    """
    Read GeoTIFF metadata and dimensions.

    Args:
        tif_name (str): Path to the input GeoTIFF file.

    Returns:
        tuple: GeoTransform, rows, and columns.
    """
    gdal.AllRegister()
    ds = gdal.Open(tif_name)
    gt = ds.GetGeoTransform()
    rows, cols = ds.RasterYSize, ds.RasterXSize

    return np.array(gt, dtype=np.double), rows, cols

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


# Function to convert geographic coordinates to intrinsic coordinates.
def convert_geographic_to_intrinsic(tif_ref: np.ndarray, lat: float, lon: float) -> Tuple[float, float]:
    """
    Convert geographic coordinates (latitude, longitude) to intrinsic coordinates.

    Args:
        tif_ref (np.ndarray): GeoTransform metadata.
        lat (float): Latitude.
        lon (float): Longitude.

    Returns:
        tuple: Intrinsic y and x coordinates.
    """
    max_lat, min_lat = tif_ref[3], tif_ref[4]
    max_lon, min_lon = tif_ref[2], tif_ref[0]
    space_lat, space_lon = tif_ref[5], tif_ref[1]

    num_lat = round(((max_lat - space_lat) - min_lat) / -space_lat)
    num_lon = round(((max_lon + space_lon) - min_lon) / space_lon)

    lat_array = np.linspace(max_lat, min_lat, num_lat)
    lon_array = np.linspace(min_lon, max_lon, num_lon)

    try:
        y = interp1d(lat_array, range(len(lat_array)))(lat)
    except ValueError:
        y = interp1d(lat_array, range(len(lat_array)), fill_value='extrapolate')(lat)

    try:
        x = interp1d(lon_array, range(len(lon_array)))(lon)
    except ValueError:
        x = interp1d(lon_array, range(len(lon_array)), fill_value='extrapolate')(lon)

    return y, x
    

# Function to convert SAR image bands into RGB format.
def convert_band_to_rgb(tif_path: str, band_number: int) -> np.ndarray:
    """
    Convert SAR image bands to RGB format.

    Args:
        tif_path (str): Path to the GeoTIFF file.
        band_number (int): Number of bands in the image.

    Returns:
        np.ndarray: RGB image as a NumPy array.
    """
    raster = gdal.Open(tif_path)

    if band_number == 3:
        bands = []
        for i in range(raster.RasterCount):
            band = raster.GetRasterBand(i + 1)
            band_data = np.array(band.ReadAsArray())

            # Normalize band data
            band_data = (band_data - band_data.min()) / (band_data.max() - band_data.min())
            bands.append(band_data)

        # Stack bands into RGB format
        rgb = np.dstack((bands[2], bands[1], bands[0]))

    elif band_number == 1:
        band_data = np.array(raster.GetRasterBand(1).ReadAsArray())
        band_data = (band_data - band_data.min()) / (band_data.max() - band_data.min())
        rgb = np.dstack((band_data, band_data, band_data))

    else:
        raise ValueError("Unsupported number of bands. Only 1 or 3 bands are supported.")

    return rgb


if __name__ == "__main__":
    
    # Example usage of the defined functions
    sample_tif = "example.tif"
    land_mask = create_land_mask(sample_tif)
    print("Land mask generated:", land_mask.shape)

    geo_transform, rows, cols = read_geotiff_metadata(sample_tif)
    print("GeoTransform:", geo_transform)

    from tifffile import imwrite
    rgb_tif = convert_band_to_rgb(sample_tif, band_number=3)
    rgb_image = np.array(rgb_tif, dtype=np.uint8)
    imwrite(save_path, rgb_image)
