from fastapi import APIRouter
from app.config.settings import settings  # 필요한 파라미터 정의 
from app.config.db_connection import get_db

# 해당하는 알고리즘, DB모델, DB서비스 import 
from app.algorithm import 
from app.models.
from app.service import 

## TODO
# 1. 인자 처리 #1: 디렉토리 관련한 인자는 모두 config/settings에 정의하여 algorithm/ 하위 파일에 할당
# 예) input_dir = settings.W01_OUTPUT_PATH 예2) geojson = settings.W03_RESOURCE_PATH + "/map.geojson"
# 2. 인자 처리 #2: 그 외 인자만 남겨두고 Query로 받도록 수정 -> 더 자세한 사항은 README.md 파일 참조 
# 예) max_hr: int = Query(alias="max-hour")
# 3. 인자 처리 #3: db: Session = Depends(get_db) 추가 -> 테이블 접근할 수 있는 DB 연결 
# 4. 함수 호출: algorithm/ 하위의 파일 호출 
# 예) w03_ready_to_use_ecmwf.ready_to_use_ecmwf(db, max_hr)
# 5. 리턴값 지정: 로그에서 확인하고 싶은 값 리턴 혹은 wait를 확인하기 위해 필요한 값 리턴
# 예) return {"max_hr": max_hr}

router = APIRouter()

@router.get("/s01")
def detect_ships(date_time: str = Query(alias="date-time"),
                      db: Session = Depends(get_db)):

    logger.info(f"======[noaa_cyclone] date_time: {date_time} ======")
    w03_ready_to_use_noaa_cyclone.ready_to_use_noaa_cyclone(db, 48, date_time)
    return {"max_hr": 48}

@router.get("/s02")
def calculate_correction(correction_map_id: str = Query(),
                         db: Session = Depends(get_db)):
    w07_calculate_correction_map.calculate_correction(db, correction_map_id)
    return {"correction_map_id": correction_map_id}


@router.get("/s03")
def calculate_navigation_risk(voyage_risk_map_id: str = Query(),
                              db: Session = Depends(get_db)):
    w08_calculate_navigation_risk.calculate_navigation_risk(db, voyage_risk_map_id)
    return {"voyage_risk_map_id": voyage_risk_map_id}
