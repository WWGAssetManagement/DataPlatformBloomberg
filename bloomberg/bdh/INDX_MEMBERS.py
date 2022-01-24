from re import L
from bloomberg.core.bds_base import BDHBase
from bloomberg.model.models import INDXMEMBERSModel

class INDX_MEMBERS(BDHBase):
    """
    blp.bhs에서 INDX_MEMBERS 필드의 값입니다. 
    """

    def __init__(self, security, **kwargs):
        super().__init__(security, self.__class__.__name__, INDXMEMBERSModel, **kwargs)


