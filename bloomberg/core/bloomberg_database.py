from sqlalchemy import Table
from config.settings import ENGINE, META


class BloombergDatabase:
    __model = None
    __table = None
    __conn = None

    def __init__(self, model):
        self.__model = model
        self.__table = self.__get_table(model)
        self.__conn = ENGINE.connect()

    def __get_table(self, model) -> Table:
        return Table(model.__tablename__, META, autoload_with=ENGINE)

    def _save(self, dict_data: list):
        """
        if you using pandas plz list dict inputs like df.to_dict('records')
        :param dict_data like  [{'col1': 1, 'col2': 0.5}, {'col1': 2, 'col2': 0.75}]
        :return:
        """
        self.__conn.execute(self.__table.insert().prefix_with("IGNORE"), dict_data)
