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
import json

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
