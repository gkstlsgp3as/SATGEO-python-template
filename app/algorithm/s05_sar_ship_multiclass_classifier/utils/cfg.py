# -*- coding: utf-8 -*-
"""
@Time          : 2024/12/18 00:00
@Author        : Shinhye Han
@File          : cfg.py
@Noice         : 
@Description   : Configuration file for ship classification tasks.
@How to use    : Import algorithm_info, training_params, and output_params from cfg.py.

@Modificattion :
    @Author    :
    @Time      :
    @Detail    :
"""

# Algorithm Information
algorithm_info = {
    "name": "Ship Classification Model",
    "description": "A deep learning-based algorithm for classifying ships from SAR images."
}

# Output Parameters
output_params = {
    "epsg": 4326,             # EPSG code for geospatial outputs
    "color_map": {            # Color mapping for visualizations
        "Cargo": (255, 0, 0),    # Red
        "Fishing": (0, 255, 0),  # Green
        "Tanker": (0, 0, 255),   # Blue
        "Sailing": (255, 255, 0),  # Yellow
        "TugTow": (255, 0, 255)   # Magenta
    },
    "file_format": "tif",     # Output file format (e.g., tif, png)
    "visualize_results": True # Whether to generate visualization of results
}
