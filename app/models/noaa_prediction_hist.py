from datetime import datetime

from sqlalchemy.orm import mapped_column, Mapped

from app.config.db_session import Base


class NoaaPredictionHist(Base):
    __tablename__ = "noaa_prediction_hist"
    __table_args__ = {'schema': 'gateway'}

    prediction_standard_time: Mapped[datetime] = mapped_column(primary_key=True, index=True)
    prediction_time: Mapped[datetime] = mapped_column(primary_key=True, index=True)

    # longitude_length: Mapped[float] = mapped_column(primary_key=True)
    # latitude_length: Mapped[float] = mapped_column(primary_key=True)
    latitude: Mapped[float] = mapped_column(primary_key=True)
    longitude: Mapped[float] = mapped_column(primary_key=True)

    pressure: Mapped[float] = mapped_column()
    water_temperature: Mapped[float] = mapped_column()

    current_speed_real: Mapped[float] = mapped_column()
    current_direction_real: Mapped[float] = mapped_column()

    wave_direction_real: Mapped[float] = mapped_column()
    wave_period: Mapped[float] = mapped_column()
    wave_height_real: Mapped[float] = mapped_column()

    wind_direction_real: Mapped[float] = mapped_column()
    wind_speed_real: Mapped[float] = mapped_column()

    update_date: Mapped[datetime] = mapped_column()
