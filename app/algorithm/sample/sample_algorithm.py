# -*- coding: utf-8 -*-
'''
@Time          : 
@Author        : 
@File          : 
@Noice         : 
@Description   : 
@How to use    : 

@Modificattion :
    @Author    :
    @Time      :
    @Detail    :
'''

import argparse
from utils.cfg import Cfg

from app.config.settings import settings
#from app.models.{모델_py_파일} import {모델_클래스}
from app.service.{서비스_py_파일} import {서비스_함수}

def sub_algorithm():
    ## 코드

def algorithm(db: Session, args: type):
    input_dir = settings.SAMPLE_INPUT_PATH
    output_dir = settings.SAMPLE_OUTPUT_PATH
    meta_file = settings.SAMPLE_META_FILE

    ## TODO
    # 원래 코드

    # 서비스 함수 호출
    # ex) bulk_upsert_ecmwf_prediction_hist(db, processed_dataframe)

''' # 인자 변경을 위한 참고용
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=ALGORITHM_NAME)
    parser.add_argument('-i', "--input_dir", type=str, required=True, default="/platform/data/inputs/, help="Path to input images")
    parser.add_argument('-o', "--output_dir", type=str, required=True, default="/platform/data/outputs/predictions.csv", help="Path to save output CSV")
    parser.add_argument('-m', '--meta_file', type=str, required=True, help="Path to meta information file")

    args = parser.parse_args()
    
    algorithm(**vars(args))
'''
    
    
