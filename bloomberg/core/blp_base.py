from datetime import datetime
from bloomberg.core.bloomberg_database import BloombergDatabase
import pandas as pd
from xbbg import blp


class BLPBase(BloombergDatabase):
    security = None
    field = None
    kwargs = None
    results = None

    def __init__(self, security, field, model, kwargs):
        super().__init__(model=model)
        self.security = security
        self.field = field
        self.kwargs = kwargs
        # self.results = self._get()

    def _check_results(self):
        if len(self.results) == 0:
            raise Exception("blp.bds의 security명이나 field명이 잘못되었습니다.")
        else:
            pass

    def _get(self):
        '''
            데이터 가져오기
            상속 받아서 오버라이딩 후 원하는 형식으로 전처리 하는 코드 만들기  
        '''
        pass

    def to_pandas(self):
        return self.results

    def to_mysql(self):
        self._save(self.results.to_dict("records"))

    def to_dict(self):
        return self.results.to_dict('records')
