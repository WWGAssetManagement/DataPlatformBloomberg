from datetime import datetime
from bloomberg.core.blp_base import BLPBase
from bloomberg.model.models import INDXMEMBERSModel
from xbbg import blp

class INDX_MEMBERS(BLPBase):
    """
    blp.bhs에서 INDX_MEMBERS 필드의 값입니다. 
    """

    def __init__(self, security, **kwargs):
        super().__init__(security, self.__class__.__name__, INDXMEMBERSModel, **kwargs)
        self._get()      
        self._check_results()  
    
    def _get(self):
        self.results = blp.bds(self.security, self.field)
        self.results['date'] = datetime.now().strftime("%Y-%m-%d")
        self.results = self.results.reset_index().rename(columns={'index':'security'})


