from datetime import datetime
from sqlalchemy import Float, Numeric
from sqlalchemy.dialects.postgresql import TIMESTAMP
from sqlalchemy.orm import mapped_column, Mapped

from app.config.db_session import Base


class KmaPredictionHist(Base):
  __tablename__ = "kma_prediction_hist"
  __table_args__ = {'schema': 'gateway'}

  prediction_standard_time: Mapped[datetime] = mapped_column(TIMESTAMP, primary_key=True)
  prediction_time: Mapped[datetime] = mapped_column(TIMESTAMP, primary_key=True)
  longitude: Mapped[float] = mapped_column(Numeric(12, 8), primary_key=True)
  latitude: Mapped[float] = mapped_column(Numeric(12, 8), primary_key=True)
  wind_u_component: Mapped[float] = mapped_column(Float)
  wind_v_component: Mapped[float] = mapped_column(Float)
  large_scale_precipitation: Mapped[float] = mapped_column(Float)
  specific_humidity: Mapped[float] = mapped_column(Float)
  relative_humidity: Mapped[float] = mapped_column(Float)
