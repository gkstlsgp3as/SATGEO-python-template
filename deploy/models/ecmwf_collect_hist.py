from datetime import datetime
from typing import List

from sqlalchemy import ARRAY, String
from sqlalchemy.dialects.postgresql import TIMESTAMP
from sqlalchemy.orm import mapped_column, Mapped

from app.config.db_session import Base


class EcmwfCollectHist(Base):
    __tablename__ = "ecmwf_collect_hist"

    transaction_id: Mapped[str] = mapped_column(primary_key=True, index=True)
    request_dates: Mapped[List[str]] = mapped_column(ARRAY(String))
    status: Mapped[str] = mapped_column(nullable=False)
    task_id: Mapped[str] = mapped_column()
    run_id: Mapped[str] = mapped_column()
    try_number: Mapped[int] = mapped_column(default=0)
    created_at: Mapped[datetime] = mapped_column(TIMESTAMP, nullable=False)
    updated_at: Mapped[datetime] = mapped_column(TIMESTAMP, nullable=False)
