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

class PXLASTModel(BASE):
    __tablename__ = "tb_px_last"
    date = Column(DATETIME)
    ticker = Column(VARCHAR(20))
    PX_LAST = Column(Float)
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
    
class NETINCOMEModel(BASE):
    __tablename__ = "tb_net_income"
    date = Column(DATETIME)
    ticker = Column(VARCHAR(20))
    NET_INCOME = Column(Float)
    __table_args__ = (
        PrimaryKeyConstraint(date, ticker),
        {},
    )

class EBITModel(BASE):
    __tablename__ = "tb_ebit"
    date = Column(DATETIME)
    ticker = Column(VARCHAR(20))
    EBIT = Column(Float)
    __table_args__ = (
        PrimaryKeyConstraint(date, ticker),
        {},
    )

class RETURNONCAPITALADJUSTEDModel(BASE):
    __tablename__ = "tb_return_on_capital_adjusted"
    date = Column(DATETIME)
    ticker = Column(VARCHAR(20))
    RETURN_ON_CAPITAL_ADJUSTED = Column(Float)
    __table_args__ = (
        PrimaryKeyConstraint(date, ticker),
        {},
    )

class ARDRDEPRECIATIONEXPModel(BASE):
    __tablename__ = "tb_ardr_depreciation_exp"
    date = Column(DATETIME)
    ticker = Column(VARCHAR(20))
    ARDR_DEPRECIATION_EXP = Column(Float)
    __table_args__ = (
        PrimaryKeyConstraint(date, ticker),
        {},
    )

class CAPITALEXPENDModel(BASE):
    __tablename__ = "tb_capital_expend"
    date = Column(DATETIME)
    ticker = Column(VARCHAR(20))
    CAPITAL_EXPEND = Column(Float)
    __table_args__ = (
        PrimaryKeyConstraint(date, ticker),
        {},
    )

class NONCASHWORKINGCAPITALModel(BASE):
    __tablename__ = "tb_non_cash_working_capital"
    date = Column(DATETIME)
    ticker = Column(VARCHAR(20))
    NON_CASH_WORKING_CAPITAL = Column(Float)
    __table_args__ = (
        PrimaryKeyConstraint(date, ticker),
        {},
    )

class TOTALINVESTEDCAPITALModel(BASE):
    __tablename__ = "tb_total_invested_capital"
    date = Column(DATETIME)
    ticker = Column(VARCHAR(20))
    TOTAL_INVESTED_CAPITAL = Column(Float)
    __table_args__ = (
        PrimaryKeyConstraint(date, ticker),
        {},
    )

class EVEBITDAADJUSTEDModel(BASE):
    __tablename__ = "tb_ev_ebitda_adjusted"
    date = Column(DATETIME)
    ticker = Column(VARCHAR(20))
    EV_EBITDA_ADJUSTED = Column(Float)
    __table_args__ = (
        PrimaryKeyConstraint(date, ticker),
        {},
    )

class EBITDAModel(BASE):
    __tablename__ = "tb_ebitda"
    date = Column(DATETIME)
    ticker = Column(VARCHAR(20))
    EBITDA = Column(Float)
    __table_args__ = (
        PrimaryKeyConstraint(date, ticker),
        {},
    )


class CURMKTCAPModel(BASE):
    __tablename__ = "tb_cur_mkt_cap"
    date = Column(DATETIME)
    ticker = Column(VARCHAR(20))
    CUR_MKT_CAP = Column(Float)
    __table_args__ = (
        PrimaryKeyConstraint(date, ticker),
        {},
    )


class BESTEVModel(BASE):
    __tablename__ = "tb_best_ev"
    date = Column(DATETIME)
    ticker = Column(VARCHAR(20))
    BEST_EV = Column(Float)
    __table_args__ = (
        PrimaryKeyConstraint(date, ticker),
        {},
    )

class CRNCYADJCURREVModel(BASE):
    __tablename__ = "tb_crncy_adj_curr_ev"
    date = Column(DATETIME)
    ticker = Column(VARCHAR(20))
    CRNCY_ADJ_CURR_EV = Column(Float)
    __table_args__ = (
        PrimaryKeyConstraint(date, ticker),
        {},
    )

class EBITDAADJUSTEDModel(BASE):
    __tablename__ = "tb_ebitda_adjusted"
    date = Column(DATETIME)
    ticker = Column(VARCHAR(20))
    EBITDA_ADJUSTED = Column(Float)
    __table_args__ = (
        PrimaryKeyConstraint(date, ticker),
        {},
    )


class CURRENTPVALModel(BASE):
    __tablename__ = "tb_current_entp_val"
    date = Column(DATETIME)
    ticker = Column(VARCHAR(20))
    CURR_ENTP_VAL = Column(Float)
    __table_args__ = (
        PrimaryKeyConstraint(date, ticker),
        {},
    )

class TRAIL12MEBITDAModel(BASE):
    __tablename__ = "tb_trail_12m_ebitda"
    date = Column(DATETIME)
    ticker = Column(VARCHAR(20))
    TRAIL_12M_EBITDA = Column(Float)
    __table_args__ = (
        PrimaryKeyConstraint(date, ticker),
        {},
    )