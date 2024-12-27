from datetime import datetime

from sqlalchemy.orm import mapped_column, Mapped

from app.config.db_session import Base
from decimal import Decimal


class SampleModel(Base): # 수정
    __tablename__ = "sample_model" # 수정
    __table_args__ = {'schema': 'gateway'}

    field1: Mapped[type] = mapped_column(primary_key=True, index=True) # 필드명 및 타입 변경, Primary Key 작성
    field2: Mapped[type] = mapped_column() # 필드명 및 타입 변경
    ...
