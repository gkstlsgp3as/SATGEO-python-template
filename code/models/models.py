# -*- coding: utf-8 -*-
"""
@Time          : 2024/12/18 00:00
@Author        : Shinhye Han
@File          : models.py
@Noice         : 
@Description   : Model definitions for XXX tasks.
@How to use    : Import Model and Bottleneck.

@Modificattion :
    @Author    :
    @Time      :
    @Detail    :
"""

import torch.nn as nn


class Bottleneck(nn.Module):
    """
    A ResNet bottleneck block.
    """

    def __init__(self, in_channels: int, out_channels: int, stride: int = 1, downsample: bool = False):
        """
        Initialize the Bottleneck block.

        Args:
            in_channels (int): Number of input channels.
            out_channels (int): Number of output channels.
            stride (int, optional): Stride for the convolutional layer. Defaults to 1.
            downsample (bool, optional): Whether to downsample the input. Defaults to False.
        """
        pass

    def forward(self, x):
        """
        Forward pass for the block.

        Args:
            x (torch.Tensor): Input tensor.

        Returns:
            torch.Tensor: Output tensor.
        """
        pass


class Model(nn.Module):
    """
    XXX model based on ResNet.
    """

    def __init__(self, block: nn.Module, layers: list, num_classes: int):
        """
        Initialize the Model.

        Args:
            block (nn.Module): The block type to use (e.g., Bottleneck).
            layers (list): List defining the number of blocks at each stage.
            num_classes (int): Number of output classes.
        """
        pass

    def forward(self, x):
        """
        Forward pass for the model.

        Args:
            x (torch.Tensor): Input tensor.

        Returns:
            torch.Tensor: Output tensor.
        """
        pass
