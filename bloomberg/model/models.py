from inspect import CO_ASYNC_GENERATOR
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

class NETOPERPROFITAFTERTAXModel(BASE):
    __tablename__ = "tb_net_oper_profit_after_tax"
    date = Column(DATETIME)
    ticker = Column(VARCHAR(20))
    NET_OPER_PROFIT_AFTER_TAX = Column(Float)
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


class ERNANNDTANDPERModel(BASE):
    __tablename__ = "tb_ern_ann_dt_and_per"
    ticker = Column(VARCHAR(20))
    earnings_announcement_date =  Column(DATETIME)	
    earnings_year_and_period = Column(VARCHAR(10))
    __table_args = (
        PrimaryKeyConstraint(ticker, earnings_announcement_date),
        {},
    )

class GICSSectorNameModel(BASE):
    __tablename__ = "tb_gics_sector_name"
    ticker = Column(VARCHAR(20), primary_key=True)
    value = Column(VARCHAR(20))


class GICSINDUSTRYNAMEModel(BASE):
    __tablename__ = "tb_gics_industry_name"
    ticker = Column(VARCHAR(20), primary_key=True)
    value = Column(VARCHAR(20))


class GICSSectorModel(BASE):
    __tablename__ = "tb_gics_sector"
    ticker = Column(VARCHAR(20), primary_key=True)
    value = Column(VARCHAR(20))


class GICSIndustryModel(BASE):
    __tablename__ = "tb_gics_industry"
    ticker = Column(VARCHAR(20), primary_key=True)
    value = Column(VARCHAR(20))


class IDCusipModel(BASE):
    __tablename__ = "tb_id_cusip"
    ticker = Column(VARCHAR(20), primary_key=True)
    value = Column(VARCHAR(20))

class SECURITYNAMEModel(BASE):
    __tablename__ = "tb_security_name"
    ticker = Column(VARCHAR(20), primary_key=True)
    value = Column(VARCHAR(20))

class PXTOBOOKRATIOModel(BASE):
    __tablename__ = "tb_px_to_book_ratio"
    date = Column(DATETIME)
    ticker = Column(VARCHAR(20))
    PX_TO_BOOK_RATIO = Column(Float)
    __table_args__ = (
        PrimaryKeyConstraint(date, ticker),
        {},
    )

class PERATIOModel(BASE):
    __tablename__ = "tb_pe_ratio"
    date = Column(DATETIME)
    ticker = Column(VARCHAR(20))
    PE_RATIO = Column(Float)
    __table_args__ = (
        PrimaryKeyConstraint(date, ticker),
        {},
    )
    