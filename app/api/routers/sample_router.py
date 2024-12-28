from fastapi import APIRouter
from app.config.settings import settings  # 필요한 파라미터 정의 
from app.config.db_connection import get_db

# 해당하는 알고리즘, DB모델, DB서비스 import 
from app.algorithm import 
from app.models.
from app.service import 

router = APIRouter()

## TODO
# 1. 인자 처리 #1: 디렉토리 관련한 인자는 모두 settings에 정의
# 예) input_dir = settings.W01_OUTPUT_PATH 예2) geojson = settings.W03_RESOURCE_PATH + "/map.geojson"
# 2. 인자 처리 #2: 그 외 인자는 Query로 받도록 수정 -> 더 자세한 사항은 README.md 파일 참조 
# 예) max_hr: int = Query(alias="max-hour")
# 3. 인자 처리 #3: db: Session = Depends(get_db) 추가 -> 테이블 접근할 수 있는 DB 연결 

@router.get("/알고리즘코드")
def 알고리즘_명(field: type = Query(alias="검색할때_사용할_이름"),
                      db: Session = Depends(get_db)):

    logger.info(f"======[알고리즘_명] field: {field} ======")
    알고리즘_py_파일명.알고리즘_명(db, field)
    return {"field": nn}
