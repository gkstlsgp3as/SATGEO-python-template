from datetime import datetime

from sqlalchemy.orm import mapped_column, Mapped

from app.config.db_session import Base

# 필요시 import
from decimal import Decimal    
from sqlalchemy import ARRAY, String
from sqlalchemy.dialects.postgresql import TIMESTAMP


class SampleModel(Base): # 수정
    __tablename__ = "sample_model" # 수정
    __table_args__ = {'schema': 'gateway'}

    field1: Mapped[type] = mapped_column(primary_key=True, index=True) # 필드명 및 타입 변경, Primary Key 작성
    field2: Mapped[type] = mapped_column() # 필드명 및 타입 변경
    ...

## 필드 종류 예시
    1) Primary Key
    longitude: Mapped[Decimal] = mapped_column(primary_key=True)   
    # 자동으로 index=True이므로 설정 불필요; 다른 필드에서 검색이 자주되는경우, index=True 설정
    # primary key는 이미 null이 비허용되므로 명시하지 않아도 됨 

    2) 타입별 정의방법
    field: Mapped[str] = mapped_column()                               # string
    field: Mapped[float] = mapped_column(Float)                        # float
    field: Mapped[int] = mapped_column()                               # int
    field: Mapped[List[str]] = mapped_column(ARRAY(String))            # List[str]
    field: Mapped[Decimal] = mapped_column()                           # 십진수; 위도/경도
    field: Mapped[datetime] = mapped_column(TIMESTAMP)                 # datetime
    
    3) 기타 설정
    field: Mapped[type] = mapped_column(nullable=False)                # null값 비허용
    field: Mapped[type] = mapped_column(default=0)                     # 디폴트 값 정의
    
    
