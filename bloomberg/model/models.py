from sqlalchemy import Column, VARCHAR, DATETIME, Float, PrimaryKeyConstraint
from config.settings import BASE


class INDXMEMBERSModel(BASE):
    __tablename__ = "tb_indx_members"
    security = Column(VARCHAR(20))
    date = Column(DATETIME)
    member_ticker_and_exchange_code = Column(VARCHAR(20))
    __table_args__ = (
        PrimaryKeyConstraint(security, date, member_ticker_and_exchange_code),
        {},
    )

class PXCLOSE1DModel(BASE):
    __tablename__ = "tb_px_close_1d"
    date = Column(DATETIME)
    ticker = Column(VARCHAR(20))
    PX_CLOSE_1D = Column(Float)
    __table_args__ = (
        PrimaryKeyConstraint(date, ticker),
        {},
    )

class PXOPENModel(BASE):
    __tablename__ = "tb_px_open"
    date = Column(DATETIME)
    ticker = Column(VARCHAR(20))
    PX_OPEN = Column(Float)
    __table_args__ = (
        PrimaryKeyConstraint(date, ticker),
        {},
    )

class PXHIGHModel(BASE):
    __tablename__ = "tb_px_high"
    date = Column(DATETIME)
    ticker = Column(VARCHAR(20))
    PX_HIGH = Column(Float)
    __table_args__ = (
        PrimaryKeyConstraint(date, ticker),
        {},
    )

class PXLOWModel(BASE):
    __tablename__ = "tb_px_low"
    date = Column(DATETIME)
    ticker = Column(VARCHAR(20))
    PX_LOW = Column(Float)
    __table_args__ = (
        PrimaryKeyConstraint(date, ticker),
        {},
    )

class PXVOLUMEModel(BASE):
    __tablename__ = "tb_px_volume"
    date = Column(DATETIME)
    ticker = Column(VARCHAR(20))
    PX_VOLUME = Column(Float)
    __table_args__ = (
        PrimaryKeyConstraint(date, ticker),
        {},
    )

class DelistModel(BASE):
    __tablename__ = "tb_delist"
    Action_Type = Column(VARCHAR(10))
    Security_ID = Column(VARCHAR(20), primary_key=True)
    Declared_Date = Column(DATETIME)
    Effective_Date = Column(DATETIME)
    Summary_1 = Column(VARCHAR(30))
    Summary_2 = Column(VARCHAR(30))
    Summary_3 = Column(VARCHAR(30))



