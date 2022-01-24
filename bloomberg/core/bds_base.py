from datetime import datetime
from bloomberg.core.bloomberg_database import BloombergDatabase 
import pandas as pd 
from xbbg import blp

class BDHBase(BloombergDatabase):
    security = None
    field = None 
    kwargs = None
    results = None

    def __init__(self, security, field, model, **kwargs):
        BloombergDatabase.__init__(self, model=model)
        self.security = security 
        self.field = field 
        self.kwargs = kwargs

    def get(self) -> pd.DataFrame:
        '''
            데이터 가져오기 
        '''
        self.results = blp.bds(self.security, self.field)
        self.results['date'] = datetime.now().strftime("%Y-%m-%d")
        return self 

    def to_pandas(self):
        return self.results

    def to_mysql(self):
        self._save(self.results.to_dict("records"))

    def to_dict(self):
        return self.results.to_dict('records')

        
        


        