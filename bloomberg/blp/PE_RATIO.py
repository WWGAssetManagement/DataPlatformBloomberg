from re import L
from bloomberg.core.blp_base import BLPBase
from bloomberg.model.models import PERATIOModel
from xbbg import blp

class PE_RATIO(BLPBase):
    """
    PER 데이터 수집 
    """
    def __init__(self, security, kwargs):
        super().__init__(security, self.__class__.__name__, PERATIOModel, kwargs)
        self._get()
        self._check_results()

    def _get(self):
        self.results = blp.bdh(self.security, self.field, self.kwargs['start'], self.kwargs['end'])
        self.results.columns.names = ['ticker', 'columns']
        self.results = self.results.T.unstack('ticker').T 
        self.results.index.names = ['date', 'ticker']
        self.results = self.results.reset_index()
