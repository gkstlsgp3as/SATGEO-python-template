# **알고리즘 네이밍 및 폴더 구조 가이드**

이 가이드는 새로운 코드를 개발할 때 사용할 네이밍 규칙과 폴더 구조를 설명합니다.

---

## **1. 네이밍 규칙**

### **a) 폴더 이름**
- **snake_case**를 사용합니다. (소문자 + 언더스코어)
- 폴더 이름은 알고리즘의 주요 기능을 **명확히 설명**해야 합니다.
- {영상데이터}_{타겟}_{기능}
- 예시:
  - `sar_ship_multiclass_classifier`: SAR 선종 분류 알고리즘
  - `sar_ship_velocity_estimator`: SAR 선박 속도 추정 알고리즘
  - `sar_ship_route_predictor`: SAR 선박 항로 예측 알고리즘

### **b) 파일 이름**
- **snake_case**를 사용합니다.
- 파일 이름은 **목적을 명확히 나타내야** 합니다.
- 예시:
  - `main.py`: 알고리즘 실행 코드
  - `classifier.py`: 분류 로직 파일
  - `preprocessing.py`: 데이터 전처리 파일
  - `postprocessing.py`: 결과 후처리 파일

---

## **2. 폴더 구조**

각 알고리즘은 다음과 같은 폴더 구조를 따라야 합니다:

## 예시
```plaintext
project/
├── deploy/                     # 배포용
│   ├── algorithm/
│   │   ├── cfg.py              # 입력 인자    
│   │   └── algorithm.py        # 알고리즘; code/ 하위 함수 통합 버전
│   ├── input/
│   │   ├── input.tif           # 입력 영상 샘플
│   │   └── metainfo.json       # 영상 metadata   
│   ├── output/
│   │   └── output.{tif/json}   # 알고리즘 실행 결과 샘플; tif, json, txt 등 
│
├── code/                       # 실제 코드
│   ├── data/                   # 데이터 관련 처리
│   ├── utils/                  # 공통 유틸리티 함수
│   ├── models/                 # 모델 학습 및 정의
│   ├── experiments/            # 실험 스크립트: 주로 ipynb 노트북 파일
│   └── main.py                 # 메인 함수
├── data/                       # 데이터 디렉토리
├── results/                    # 결과 디렉토리
│   ├── logs/                   # 로그 데이터
│   ├── figures/                # 시각화 결과
│   ├── models/                 # 학습된 모델 저장
│   └── reports/                # 분석 결과
├── requirements.txt            # 의존성 패키지 목록
├── .gitignore                  # git push 제외 목록
└── README.md                   # 프로젝트 설명 파일: 설치 과정, 훈련/추론 명령어 등

