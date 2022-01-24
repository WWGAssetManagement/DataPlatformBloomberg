from bloomberg.bdh.INDX_MEMBERS import INDX_MEMBERS

def get_indx_members(security, **kwargs):
    return INDX_MEMBERS(security=security, **kwargs)