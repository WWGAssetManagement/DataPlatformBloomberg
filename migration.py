from config.settings import ENGINE
from bloomberg.model.models import INDXMEMBERSModel, PXCLOSE1DModel


INDXMEMBERSModel.__table__.create(bind=ENGINE, checkfirst=True)
PXCLOSE1DModel.__table__.create(bind=ENGINE, checkfirst=True)