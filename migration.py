from config.settings import ENGINE
from bloomberg.model.models import INDXMEMBERSModel


INDXMEMBERSModel.__table__.create(bind=ENGINE, checkfirst=True)
