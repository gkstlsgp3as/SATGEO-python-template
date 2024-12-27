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
    dates: Mapped[List[str]] = mapped_column(ARRAY(String))            # List[str]
    status: Mapped[str] = mapped_column(nullable=False)                # null값 비허용, str
    try_number: Mapped[int] = mapped_column(default=0)                 # 디폴트 값 정의, int 
    created_at: Mapped[datetime] = mapped_column(TIMESTAMP, nullable=False)    # 시간
    longitude: Mapped[Decimal] = mapped_column(primary_key=True, index=True)   # 십진수, primary key, index=True
    latitude: Mapped[float] = mapped_column(primary_key=True)                  # primary key, index=False
    longitude_length: Mapped[float] = mapped_column()                  # float
    
    
