from datetime import datetime
from bloomberg.core.bds_base import BDHBase
from bloomberg.model.models import INDXMEMBERSModel

class INDX_MEMBERS(BDHBase):
    """
    blp.bhs에서 INDX_MEMBERS 필드의 값입니다. 
    """

    def __init__(self, security, **kwargs):
        super().__init__(security, self.__class__.__name__, INDXMEMBERSModel, **kwargs)
        self._data_preprocessing()

    def _data_preprocessing(self):
        self.results['date'] = datetime.now().strftime("%Y-%m-%d")
        self.results.reset_index().rename(columns={'index':'security'})
