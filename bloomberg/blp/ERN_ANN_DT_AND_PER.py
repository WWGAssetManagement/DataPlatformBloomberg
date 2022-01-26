from bloomberg.core.blp_base import BLPBase
from bloomberg.model.models import ERNANNDTANDPERModel
from xbbg import blp

class ERN_ANN_DT_AND_PER(BLPBase):
    """
    blp.bhs에서 ERN_ANN_DT_AND_PER 필드의 값입니다. 
    """

    def __init__(self, security, **kwargs):
        super().__init__(security, self.__class__.__name__, ERNANNDTANDPERModel, **kwargs)
        self._get()      
        self._check_results()  
    
    def _get(self):
        self.results = blp.bds(self.security, self.field)
        self.results = self.results.reset_index().rename(columns={'index':'ticker'})








