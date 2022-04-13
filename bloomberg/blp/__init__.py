import imp
from bloomberg.blp.ERN_ANN_DT_AND_PER import ERN_ANN_DT_AND_PER
from bloomberg.blp.INDX_MEMBERS import INDX_MEMBERS
from bloomberg.blp.PX_CLOSE_1D import PX_CLOSE_1D
from bloomberg.blp.PX_OPEN import PX_OPEN
from bloomberg.blp.PX_HIGH import PX_HIGH
from bloomberg.blp.PX_LOW import PX_LOW
from bloomberg.blp.PX_VOLUME import PX_VOLUME
from bloomberg.blp.GICS_SECTOR_NAME import GICS_SECTOR_NAME
from bloomberg.blp.GICS_INDUSTRY_NAME import GICS_INDUSTRY_NAME
from bloomberg.blp.GICS_SECTOR import GICS_SECTOR
from bloomberg.blp.GICS_INDUSTRY import GICS_INDUSTRY
from bloomberg.blp.ID_CUSIP import ID_CUSIP
from bloomberg.blp.NET_OPER_PROFIT_AFTER_TAX import NET_OPER_PROFIT_AFTER_TAX
from bloomberg.blp.SECURITY_NAME import SECURITY_NAME
from bloomberg.blp.PE_RATIO import PE_RATIO
from bloomberg.blp.PX_TO_BOOK_RATIO import PX_TO_BOOK_RATIO
from bloomberg.blp.PX_LAST import PX_LAST
from bloomberg.blp.NET_INCOME import NET_INCOME
from bloomberg.blp.EBIT import EBIT
from bloomberg.blp.RETURN_ON_CAPITAL_ADJUSTED import RETURN_ON_CAPITAL_ADJUSTED

def get_indx_members(security, **kwargs):
    return INDX_MEMBERS(security=security, kwargs=kwargs)


def get_px_close_1d(security, **kwargs):
    return PX_CLOSE_1D(security=security, kwargs=kwargs)


def get_px_last(sercurity, **kwargs):
    return PX_LAST(security=sercurity, kwargs=kwargs)


def get_px_open(security, **kwargs):
    return PX_OPEN(security=security, kwargs=kwargs)


def get_px_high(security, **kwargs):
    return PX_HIGH(security=security, kwargs=kwargs)


def get_px_low(security, **kwargs):
    return PX_LOW(security=security, kwargs=kwargs)


def get_px_volume(security, **kwargs):
    return PX_VOLUME(security=security, kwargs=kwargs)


def get_ern_ann_dt_and_per(security, **kwargs):
    return ERN_ANN_DT_AND_PER(security=security, kwargs=kwargs)

def get_pe_ratio(security, **kwargs):
    return PE_RATIO(security=security, kwargs=kwargs)

def get_px_to_book_ratio(security, **kwargs):
    return PX_TO_BOOK_RATIO(security=security, kwargs=kwargs)

def get_net_income(security, **kwargs):
    return NET_INCOME(security=security, kwargs=kwargs)

def get_ebit(security, **kwargs):
    return EBIT(security=security, kwargs=kwargs)

def get_return_on_capital_adjusted(security, **kwargs):
    return RETURN_ON_CAPITAL_ADJUSTED(security=security, kwargs=kwargs)

def get_gics_sector_name(security, **kwargs):
    return GICS_SECTOR_NAME(security=security, kwargs=kwargs)


def get_gics_industry_name(security, **kwargs):
    return GICS_INDUSTRY_NAME(security=security, kwargs=kwargs)


def get_gics_sector(security, **kwargs):
    return GICS_SECTOR(security=security, kwargs=kwargs)


def get_gics_industry(security, **kwargs):
    return GICS_INDUSTRY(security=security, kwargs=kwargs)


def get_id_cusip(security, **kwargs):
    return ID_CUSIP(security=security, kwargs=kwargs)


def get_net_oper_profit_after_tax(security, **kwargs):
    return NET_OPER_PROFIT_AFTER_TAX(security=security, kwargs=kwargs)


def get_security_name(security, **kwargs):
    return SECURITY_NAME(security=security, kwargs=kwargs)
