from fastapi import APIRouter
from app.config.settings import settings  # 필요한 파라미터 정의 
from app.config.db_connection import get_db

# 해당하는 알고리즘, DB모델, DB서비스 import 
from app.algorithm import 
from app.models.
from app.service import 

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
