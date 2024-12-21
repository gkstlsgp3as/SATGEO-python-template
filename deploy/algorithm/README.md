🎉 Feat: "S05_ShipCls"

## 내용
재초점화 칩셋 내 선종 식별
식별 모델 정의, 데이터셋 정의, 데이터 전처리 등

## 실행 명령어
```sh
python SAR_shipmultcls.py --img_path {이미지 경로} --meta-file {메타파일 경로} 
```

## 입출력 및 폴더 구조
.     
├── input (재초점화 선박 칩 입력 샘플) -> 추후 DB로부터 경로/데이터 로드    
│ └── ICEYE     
│  　 └── Cargo_03.tif   
│  　 ├── Cargo_07.tif    
│ 　  ├── Fishing_03.tif   
│ 　  ├── Others_26.tif   
│  　 ├── Sailing_05.tif   
│  　 ├── Tanker_01.tif   
│  　 ├── Tanker_05.tif   
│  　 └── TugTow_01.tif   
├── utils   
│ └── datasets.py (데이터셋 정의 코드)   
├── models   
│ ├── misc.py (모델 생성 코드)   
│ ├── shipclsmodel.py (모델 구조 정의 코드)   
│ └── weights   
│ └── ICEYE.pt (사전 학습 모델)   
├── output   
│ └── pred.csv (샘플 출력 파일) -> 추후 DB에 업데이트    
├── metainfo.json (위성 영상 메타데이터 샘플)    
└── SAR_shipmultcls.py (main 실행 함수)   

Resolves: #4
