from bloomberg.core.blp_base import BLPBase
from bloomberg.model.models import GICSIndustryModel
from xbbg import blp

class GICS_INDUSTRY(BLPBase):
    """
    blp.bdh에서 GICS_INDUSTRY 필드의 값입니다. 
    """

    def __init__(self, security, **kwargs):
        super().__init__(security, self.__class__.__name__, GICSIndustryModel, **kwargs)
        self._get()      
        self._check_results()  
    
    def _get(self):
        self.results = blp.bds(self.security, self.field)
        self.results = self.results.reset_index().rename(columns={'index':'ticker'})


   