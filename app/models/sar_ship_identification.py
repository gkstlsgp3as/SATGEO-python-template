from sqlalchemy.orm import mapped_column, Mapped
from app.config.db_session import Base


class SarShipIdentification(Base):
  __tablename__ = "sar_ship_identification"
  __table_args__ = {'schema': 'gateway'}

  satellite_sar_image_id: Mapped[str] = mapped_column(String(32), primary_key=True)
  identification_ship_id: Mapped[str] = mapped_column(String(64), primary_key=True)
  longitude: Mapped[float] = mapped_column(Numeric(12, 8))
  latitude: Mapped[float] = mapped_column(Numeric(12, 8))
  interpolation_cog: Mapped[float] = mapped_column(Float)
  interpolation_sog: Mapped[float] = mapped_column(Float)
  type: Mapped[str] = mapped_column(String(10))
  end: Mapped[str] = mapped_column(String(10))
  detection_yn: Mapped[bool] = mapped_column()
  detection_longitude: Mapped[float] = mapped_column(Float)
  detection_latitude: Mapped[float] = mapped_column(Float)
