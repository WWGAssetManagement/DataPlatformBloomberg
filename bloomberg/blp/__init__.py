import imp
from bloomberg.blp.INDX_MEMBERS import INDX_MEMBERS
from bloomberg.blp.PX_CLOSE_1D import PX_CLOSE_1D
from bloomberg.blp.PX_OPEN import PX_OPEN
from bloomberg.blp.PX_HIGH import PX_HIGH
from bloomberg.blp.PX_LOW import PX_LOW


def get_indx_members(security, **kwargs):
    return INDX_MEMBERS(security=security, kwargs=kwargs)


def get_px_close_1d(security, **kwargs):
    return PX_CLOSE_1D(security=security, kwargs=kwargs)


def get_px_open(security, **kwargs):
    return PX_OPEN(security=security, kwargs=kwargs)


def get_px_high(security, **kwargs):
    return PX_HIGH(security=security, kwargs=kwargs)


def get_px_low(security, **kwargs):
    return PX_LOW(security=security, kwargs=kwargs)


