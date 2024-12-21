# **알고리즘 네이밍 및 폴더 구조 가이드**

이 가이드는 새로운 코드를 개발할 때 사용할 네이밍 규칙과 폴더 구조를 설명합니다.

---

## **1. 네이밍 규칙**

### **a) 폴더 이름**
- **snake_case**를 사용합니다. (소문자 + 언더스코어)
- 폴더 이름은 알고리즘의 주요 기능을 **명확히 설명**해야 합니다.
- ```{영상데이터}_{타겟}_{기능}```
- 예시:
  - `sar_ship_multiclass_classifier`: SAR 선종 분류 알고리즘
  - `sar_ship_velocity_estimator`: SAR 선박 속도 추정 알고리즘
  - `sar_ship_route_predictor`: SAR 선박 항로 예측 알고리즘

### **b) 파일 이름**
- **snake_case**를 사용합니다.
- 파일 이름은 **목적을 명확히 나타내야** 합니다.
- 예시:


| **목적**              | **파일 이름 예시**          | **설명**                                     |
|-----------------------|----------------------------|---------------------------------------------|
| 실행 코드             | `main.py`                 | 알고리즘 실행을 위한 진입점 코드             |
| 분류 로직             | `classifier.py`           | 분류 알고리즘의 핵심 로직 코드               |
| 데이터 전처리          | `preprocessing.py`        | 입력 데이터를 전처리하는 코드                |
| 결과 후처리           | `postprocessing.py`       | 알고리즘 결과를 후처리하는 코드              |
| 설정 파일             | `cfg.py`                  | 알고리즘 매개변수를 관리하는 설정 파일        |
| 모델 정의             | `model.py`                | 모델의 구조 및 초기화 코드                   |
| 유틸리티 함수         | `utils.py`                | 공통으로 사용하는 유틸리티 함수 코드         |
| 데이터셋 처리         | `dataset.py`              | 데이터셋 로드 및 처리 관련 코드              |
| 시각화 코드           | `visualization.py`        | 결과를 시각화하는 코드                       |

### **c) 클래스 이름**
- **PascalCase**를 사용합니다. (각 단어의 첫문자 대문자)
- 클래스 이름은 기능을 명확히 나타내며, 간결하고 설명적이어야 합니다.
- 일반적으로 잘 알려져 있거나 널리 사용되는 경우에만 사용합니다.
- 예시:
  - ShipClassificationModel: 선박 분류를 위한 딥러닝 모델 클래스.
  - Bottleneck: ResNet의 Bottleneck 블록을 나타내는 클래스.
  - ShipClassificationDataset: 선박 분류 작업을 위한 데이터셋 클래스.
  - TiffProcessor: TIFF 파일을 처리하는 유틸리티 클래스.
 

### **d) 함수 이름**
- **snake_case**를 사용합니다. (각 단어의 첫문자 대문자)
- 함수는 주로 동작을 수행하므로, 동사로 시작하여 기능을 명확히 표현합니다.
- 예시:
  - load_image: 이미지를 로드.
  - process_data: 데이터를 처리.
  - train_model: 모델 학습.
---

## **2. 폴더 구조**
각 알고리즘은 다음과 같은 폴더 구조를 따라야 합니다:
## 예시
```plaintext
project/
├── deploy/                     # 배포용
│   ├── algorithm/
│   │   ├── utils/              # 데이터 처리 등 기타 유틸리티 함수
│   │   ├── models/             # 모델 정의  
│   │   ├── algorithm.py        # 알고리즘; code/ 하위 함수 통합 버전
│   │   ├── requirements.txt            # 의존성 패키지 목록
│   │   ├── .gitignore                  # git push 제외 목록
│   │   └── README.md                   # 프로젝트 설명 파일: 설치 과정, 훈련/추론 명령어 등
│   ├── input/
│   │   ├── input.tif           # 입력 영상 샘플
│   │   └── metainfo.json       # 영상 metadata   
│   ├── output/
│   │   └── output.{tif/json}   # 알고리즘 실행 결과 샘플; tif, json, txt 등 
│
├── code/                       # 실제 코드
│   ├── utils/                  # 데이터 처리 등 기타 유틸리티 함수
│   ├── models/                 # 모델 정의
│   ├── experiments/            # 실험 스크립트: 주로 ipynb 노트북 파일
│   ├── main.py                 # 메인 함수
│   ├── requirements.txt            # 의존성 패키지 목록
│   ├── .gitignore                  # git push 제외 목록
│   └── README.md                   # 프로젝트 설명 파일: 설치 과정, 훈련/추론 명령어 등
├── data/                       # 데이터 디렉토리
├── results/                    # 결과 디렉토리
│   ├── logs/                   # 로그 데이터
│   ├── figures/                # 시각화 결과
│   ├── models/                 # 학습된 모델 저장
│   └── reports/                # 분석 결과
```

---
## **3. 체크리스트**
✅ **PEP8 스타일 준수**: 모든 코드가 Python의 PEP8 스타일 가이드를 준수하는지 확인

✅ **입출력 파일 구조 확인**: `input_dir`과 `output_dir` 경로 설정을 확인

✅ **배포 코드**: 필수 함수를 포함한 단일 파일 제작 여부 확인

✅ **주석 설명**: 코드 주요 부분에 주석 및 설명 추가

✅ **문서화**: 프로젝트의 메인 `README.md`에 알고리즘 설명 및 실행 방법 추가
