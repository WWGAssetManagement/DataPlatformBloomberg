from datetime import datetime
from bloomberg.core.blp_base import BLPBase
from bloomberg.model.models import NETOPERPROFITAFTERTAXModel
from xbbg import blp

class NET_OPER_PROFIT_AFTER_TAX(BLPBase):
    """
    blp.bhs에서 NET_OPER_PROFIT_AFTER_TAX 필드의 값입니다. 
    """

    def __init__(self, security, kwargs):
        super().__init__(security, self.__class__.__name__, NETOPERPROFITAFTERTAXModel, kwargs)
        self._get()
        self._check_results()

    def _get(self):
        self.results = blp.bdh(self.security, self.field, self.kwargs['start'], self.kwargs['end'])
        self.results.columns.names = ['ticker', 'columns']
        self.results = self.results.T.unstack('ticker').T 
        self.results.index.names = ['date', 'ticker']
        self.results = self.results.reset_index()
