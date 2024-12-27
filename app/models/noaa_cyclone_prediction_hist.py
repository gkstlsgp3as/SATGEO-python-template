from datetime import datetime

from sqlalchemy.orm import mapped_column, Mapped

from app.config.db_session import Base


class NoaaCyclonePredictionHist(Base):
    __tablename__ = "noaa_cyclone_prediction_hist"
    __table_args__ = {'schema': 'gateway'}

    prediction_standard_time: Mapped[datetime] = mapped_column(primary_key=True, index=True)
    prediction_time: Mapped[datetime] = mapped_column(primary_key=True, index=True)

    latitude: Mapped[float] = mapped_column(primary_key=True)
    longitude: Mapped[float] = mapped_column(primary_key=True)

    pressure: Mapped[float] = mapped_column()
    wind_speed_real: Mapped[float] = mapped_column()

    update_date: Mapped[datetime] = mapped_column()
