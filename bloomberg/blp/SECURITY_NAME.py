from tkinter import image_names
from bloomberg.core.blp_base import BLPBase
from bloomberg.model.models import SECURITYNAMEModel
from xbbg import blp 


class SECURITY_NAME(BLPBase):
    """
    Security 이름을 가져오는 클래스 입니다. 
    """

    def __init__(self, security, **kwargs):
        super().__init__(security, self.__class__.__name__, SECURITYNAMEModel, kwargs)
        self._get()      
        self._check_results() 

    def _get(self):
        self.results = blp.bds(self.security, self.field)
        self.results = self.results.reset_index().rename(columns={'index':'ticker'})
