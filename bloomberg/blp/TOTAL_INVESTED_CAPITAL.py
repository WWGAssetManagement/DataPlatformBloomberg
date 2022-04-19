from bloomberg.core.blp_base import BLPBase
from bloomberg.model.models import TOTALINVESTEDCAPITALModel
from xbbg import blp

class TOTAL_INVESTED_CAPITAL(BLPBase):
    """
    TOTAL_INVESTED_CAPITAL 데이터 수집 
    """
    def __init__(self, security, kwargs):
        super().__init__(security, self.__class__.__name__, TOTALINVESTEDCAPITALModel, kwargs)
        self._get()
        self._check_results()

    def _get(self):
        self.results = blp.bdh(self.security, self.field, self.kwargs['start'], self.kwargs['end'])
        self.results.columns.names = ['ticker', 'columns']
        self.results = self.results.T.unstack('ticker').T 
        self.results.index.names = ['date', 'ticker']
        self.results = self.results.reset_index()
        