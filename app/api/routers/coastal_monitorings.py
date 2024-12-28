from fastapi import APIRouter
from app.config.settings import settings  # 필요한 파라미터 정의 
from app.config.db_connection import get_db

# 해당하는 알고리즘, DB모델, DB서비스 import 
from app.algorithm import m01_coregister_images, m02_create_quickview_animation, m03_extract_rois, \
                          m04_detect_displacement, m05_detect_changes_acd, m06_detect_changes_mad, \
                          m07_detect_ships, m08_detect_aircrafts, m09_detect_vehicles, m10_detect_building_changes \
                          m11_detect_container_changes, m12_estimate_sst, m13_detect_oil_spills

from app.models.roi_last import RoiLast

from app.service import roi_last_service

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

@router.get("/m01")
def coregister_images(satellite_sar_image_id: str = Query(...)):
    m01_coregister_images.coregister_images(satellite_sar_image_id)
    return {"satellite_sar_image_id": satellite_sar_image_id}


@router.get("/m02")
def create_quickview_animation(facility_id: str = Query(),
                         db: Session = Depends(get_db)):
    m02_create_quickview_animation.create_quickview_animation(db, facility_id)
    return {"facility_id": facility_id}


@router.get("/m03")
def extract_rois(facility_id: str = Query(),
                              db: Session = Depends(get_db)):
    m03_extract_rois.extract_rois(db, facility_id)
    return {"facility_id": facility_id}


@router.get("/m04")
def detect_displacement(interest_area_image_id: str = Query(),
                              db: Session = Depends(get_db)):
    m04_detect_displacement.detect_displacement(db, interest_area_image_id)
    return {"interest_area_image_id": interest_area_image_id}


@router.get("/m05")
def detect_changes_acd(interest_area_image_id: str = Query(),
                              db: Session = Depends(get_db)):
    m05_detect_changes_acd.detect_changes_acd(db, interest_area_image_id)
    return {"interest_area_image_id": interest_area_image_id}


@router.get("/m06")
def detect_changes_mad(interest_area_image_id: str = Query(),
                              db: Session = Depends(get_db)):
    m06_detect_changes_mad.detect_changes_mad(db, interest_area_image_id)
    return {"interest_area_image_id": interest_area_image_id}


@router.get("/m07")
def detect_ships(interest_area_image_id: str = Query(),
                              db: Session = Depends(get_db)):
    m07_detect_ships.detect_ships(db, interest_area_image_id)
    return {"interest_area_image_id": interest_area_image_id}


@router.get("/m08")
def detect_aircrafts(interest_area_image_id: str = Query(),
                              db: Session = Depends(get_db)):
    m08_detect_aircrafts.detect_aircrafts(db, interest_area_image_id)
    return {"interest_area_image_id": interest_area_image_id}


@router.get("/m09")
def detect_vehicles(interest_area_image_id: str = Query(),
                              db: Session = Depends(get_db)):
    m09_detect_vehicles.detect_vehicles(db, interest_area_image_id)
    return {"interest_area_image_id": interest_area_image_id}


@router.get("/m10")
def detect_building_changes(interest_area_image_id: str = Query(),
                              db: Session = Depends(get_db)):
    m10_detect_building_changes.detect_building_changes(db, interest_area_image_id)
    return {"interest_area_image_id": interest_area_image_id}


@router.get("/m11")
def detect_container_changes(interest_area_image_id: str = Query(),
                              db: Session = Depends(get_db)):
    m11_detect_container_changes.detect_container_changes(db, interest_area_image_id)
    return {"interest_area_image_id": interest_area_image_id}


@router.get("/m12")
def estimate_sst(interest_area_image_id: str = Query(),
                              db: Session = Depends(get_db)):
    m12_estimate_sst.estimate_sst(db, interest_area_image_id)
    return {"interest_area_image_id": interest_area_image_id}


@router.get("/m13")
def detect_oil_spills(interest_area_image_id: str = Query(),
                              db: Session = Depends(get_db)):
    m13_detect_oil_spills.detect_oil_spills(db, interest_area_image_id)
    return {"interest_area_image_id": interest_area_image_id}
