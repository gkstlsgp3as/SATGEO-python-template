# -*- coding: utf-8 -*-
"""
@Time          : 2024/12/18 00:00
@Author        : Shinhye Han
@File          : datasets.py
@Noice         : 
@Description   : Dataset definitions for XXX tasks.
@How to use    : Import Dataset for training and evaluation.

@Modificattion :
    @Author    :
    @Time      :
    @Detail    :
"""

from pathlib import Path
from typing import List
from PIL import Image
from torch.utils.data import Dataset


class Dataset(Dataset):
    """
    Dataset for XXX tasks.
    """

    def __init__(self, data_dir: str, classes: List[str], transforms=None):
        """
        Initialize the dataset.

        Args:
            data_dir (str): Path to the directory containing images.
            classes (List[str]): List of class labels.
            transforms (optional): Transformations to apply to the images.
        """
        pass

    def __len__(self) -> int:
        """
        Return the number of samples in the dataset.

        Returns:
            int: Number of samples.
        """
        pass

    def __getitem__(self, idx: int):
        """
        Retrieve a single sample from the dataset.

        Args:
            idx (int): Index of the sample to retrieve.

        Returns:
            tuple: Image and its corresponding label.
        """
        pass
