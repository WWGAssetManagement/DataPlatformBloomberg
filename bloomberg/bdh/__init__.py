import imp
from bloomberg.bdh.INDX_MEMBERS import INDX_MEMBERS
from bloomberg.bdh.PX_CLOSE_1D import PX_CLOSE_1D

def get_indx_members(security, **kwargs):
    return INDX_MEMBERS(security=security, kwargs=kwargs)

def get_px_close_1d(security, **kwargs):
    return PX_CLOSE_1D(security=security, kwargs=kwargs)
    