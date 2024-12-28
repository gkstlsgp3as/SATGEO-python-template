from fastapi import APIRouter
from app.config.settings import settings  # 필요한 파라미터 정의 
from app.config.db_connection import get_db

# 해당하는 알고리즘, DB모델, DB서비스 import 
from app.algorithm import n01_detect_all_facilities, n02_synchronize_ais_time, n03_detect_ships_high_recall, \
                          n04_remove_known_facilities, n05_generate_statistics, n06_update_known_facilities

from app.models.new_facilities_hist import NewFacilitiesHist
from app.models.known_facilities_hist import KnownFacilitiesHist

from app.service import new_facilities_hist_service, known_facilities_hist_service

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

@router.get("/n01")
def detect_all_facilities(satellite_sar_image_id: str = Query(...)):
    n01_detect_all_facilities.detect_all_facilities(satellite_sar_image_id)
    return {"satellite_sar_image_id": satellite_sar_image_id}


@router.get("/n02")
def synchronize_ais_time(satellite_sar_image_id: str = Query(),
                         db: Session = Depends(get_db)):
    n02_synchronize_ais_time.synchronize_ais_time(db, satellite_sar_image_id)
    return {"satellite_sar_image_id": satellite_sar_image_id}


@router.get("/n03")
def detect_ships_high_recall(satellite_sar_image_id: str = Query(),
                              db: Session = Depends(get_db)):
    n03_detect_ships_high_recall.detect_ships_high_recall(db, satellite_sar_image_id)
    return {"satellite_sar_image_id": satellite_sar_image_id}


@router.get("/n04")
def remove_known_facilities(facility_id: str = Query(),
                              db: Session = Depends(get_db)):
    n04_remove_known_facilities.remove_known_facilities(db, facility_id)
    return {"facility_id": facility_id}


@router.get("/n05")
def generate_statistics(date: str = Query(),
                              db: Session = Depends(get_db)):
    n05_generate_statistics.generate_statistics(db, date)
    return {"date": date}


@router.get("/n06")
def update_known_facilities(facility_id: str = Query(),
                              db: Session = Depends(get_db)):
    n06_update_known_facilities.update_known_facilities(db, facility_id)
    return {"facility_id": facility_id}
