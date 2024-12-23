# **알고리즘 네이밍 및 폴더 구조 가이드**

본 가이드는 SATGEO 내에서 코드를 개발할 때 사용할 네이밍 규칙과 폴더 구조를 설명합니다.

---

## **1. 네이밍 규칙**

### **a) 폴더 이름**
- **snake_case** 사용 (소문자 + 언더스코어)
- 폴더 이름은 알고리즘의 **주요 기능**을 명확히 설명
- ```{영상데이터}_{대상}_{기능}```
- 영상 데이터는 필요 시 생략 가능 
- 예시:
  - `sar_ship_multiclass_classifier`: SAR 선종 분류 알고리즘
  - `sar_ship_velocity_estimator`: SAR 선박 속도 추정 알고리즘
  - `sar_ship_route_predictor`: SAR 선박 항로 예측 알고리즘

### **b) 파일 이름**
- **snake_case** 사용
- 파일 이름은 아래의 기능에 따른 분류를 포함하도록 작성
- 기능 분류

| **목적**              | **파일 이름 예시**          | **설명**                                     |
|-----------------------|----------------------------|---------------------------------------------|
| 실행 코드             | `main.py`                 | 알고리즘 실행을 위한 진입점 코드             |
| 훈련 코드             | `train.py`                | 딥러닝 모델 훈련 코드                        |
| 추론 코드             | `inference.py`            | 딥러닝 모델 추론 코드                        |
| 분류 로직             | `classifier.py`           | 분류 알고리즘의 핵심 로직 코드               |
| 데이터 전처리         | `preprocessing.py`        | 입력 데이터를 전처리하는 코드                |
| 결과 후처리           | `postprocessing.py`       | 알고리즘 결과를 후처리하는 코드              |
| 설정 파일             | `cfg.py`                  | 알고리즘 매개변수를 관리하는 설정 파일        |
| 모델 정의             | `models.py`                | 모델의 구조 및 초기화 코드                   |
| 유틸리티 함수         | `utils.py`                | 공통으로 사용하는 유틸리티 함수 코드         |
| 데이터셋 처리         | `datasets.py`              | 데이터셋 로드 및 처리 관련 코드              |
| 시각화 코드           | `visualization.py`        | 결과를 시각화하는 코드                       |

- 예시: main.py, torch_utils.py, resnet_model.py, dataset.py 등

### **c) 클래스 이름**
- **PascalCase** 사용 (각 단어의 첫문자 대문자)
- 클래스 이름은 기능을 명확히 설명
- 일반적으로 잘 알려져 있는 경우에만 약어 사용
- 예시:
  - ShipClassificationModel: 선박 분류를 위한 딥러닝 모델 클래스
  - Bottleneck: ResNet의 Bottleneck 블록을 나타내는 클래스
  - ShipClassificationDataset: 선박 분류 작업을 위한 데이터셋 클래스
  - TiffProcessor: TIFF 파일을 처리하는 유틸리티 클래스
 

### **d) 함수 이름**
- **snake_case** 사용 (각 단어의 첫문자 대문자)
- ```{동사}_{대상}```
- 예시:
  - load_image: 이미지를 로드
  - process_data: 데이터를 처리
  - train_model: 모델 학습

### **e) 상수 이름**
- **UPPER_CASE** 사용 (전부 대문자)
- 예시: ```MAX_EPOCHS = 100```
---

## **2. 폴더 구조**
각 알고리즘은 다음의 폴더 구조를 따라야 함: 
## 예시
```plaintext
project/
├── deploy/                     # 배포용
│   ├── algorithm/
│   │   ├── utils/              # 데이터 처리 등 기타 유틸리티 함수
│   │   ├── models/             # 모델 정의  
│   │   ├── algorithm.py        # 알고리즘; code/ 하위 알고리즘1 통합 버전
│   │   ├── requirements.txt    # 의존성 패키지 목록
│   │   ├── .gitignore          # git push 제외 목록
│   │   └── README.md           # 프로젝트 설명 파일: 설치 과정, 훈련/추론 명령어 등
│   ├── algorithm2/
│   │   ├── algorithm2.py        # 알고리즘; code/ 하위 알고리즘2 통합 버전
│   ├── input/
│   │   ├── input.tif           # 입력 영상 샘플
│   │   └── metainfo.json       # 영상 metadata   
│   ├── output/
│   │   └── output.{tif/json}   # 알고리즘 실행 결과 샘플; tif, json, txt 등 
│
├── code/                       # 실제 코드
│   ├── utils/                  # 데이터 처리 등 기타 유틸리티 함수
│   ├── models/                 # 모델 정의
│   ├── experiments/            # 실험: 주로 ipynb 노트북 파일
│   ├── scripts/                # 실행 스크립트: .sh 파일 등
│   ├── main.py                 # 메인 함수
│   ├── requirements.txt        # 의존성 패키지 목록
│   ├── .gitignore              # git push 제외 목록
│   └── README.md               # 프로젝트 설명 파일: 설치 과정, 훈련/추론 명령어 등
├── data/                       # 데이터 디렉토리
│   ├── raw/                    # 원본 데이터 
│   ├── processed/              # 가공 데이터
│   ├── train/                  # 학습/검증/테스트 데이터 분할
│   ├── val/        
│   └── test/        
├── results/                    # 결과 디렉토리
│   ├── logs/                   # 로그 데이터
│   ├── figures/                # 시각화 결과
│   ├── models/                 # 학습된 모델 저장
│   └── reports/                # 분석 결과
```

---
## **3. 체크리스트**
✅ **PEP 484 스타일 준수**: 모든 코드가 Python의 PEP 484 스타일 가이드를 준수하는지 확인 - ChatGPT 활용

✅ **입출력 파일 구조 확인**: `input_dir`과 `output_dir` 경로 설정 확인

✅ **배포 코드**: 필수 함수만을 포함한 파일 제작 여부 확인. Dockerfile과의 호환 여부 확인. 

✅ **주석 설명**: 코드 주요 부분에 주석 및 설명 추가

✅ **문서화**: 프로젝트의 메인 `README.md`에 알고리즘 설명 및 실행 방법 추가
