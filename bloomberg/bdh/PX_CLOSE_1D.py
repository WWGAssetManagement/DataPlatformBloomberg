from datetime import datetime
from bloomberg.core.bds_base import BDHBase
from bloomberg.model.models import PXCLOSE1DModel
from xbbg import blp

class PX_CLOSE_1D(BDHBase):
    """
    blp.bhs에서 PX_CLOSE_1D 필드의 값입니다. 
    """

    def __init__(self, security, kwargs):
        super().__init__(security, self.__class__.__name__, PXCLOSE1DModel, kwargs)
        self._get()
        self._check_results()

    def _get(self):
        self.results = blp.bdh(self.security, self.field, self.kwargs['start'], self.kwargs['end'])
        self.results.columns.names = ['ticker', 'columns']
        self.results = self.results.T.unstack('ticker').T 
        self.results.index.names = ['date', 'ticker']
        self.results = self.results.reset_index()
