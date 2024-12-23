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

# Inference Information
aux_path = "./data/landmask/landmask.tif"        # 그 외 다른 입력 자료 경로
weights = "./models/weights/best.pth"            # 모델 경로 
device = "cuda:0"                                # GPU 지정 
