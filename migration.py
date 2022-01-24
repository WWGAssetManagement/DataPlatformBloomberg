from config.settings import ENGINE
from bloomberg.model.models import(
    INDXMEMBERSModel, 
    PXCLOSE1DModel,
    PXOPENModel,
    PXLOWModel,
    PXVOLUMEModel
)


INDXMEMBERSModel.__table__.create(bind=ENGINE, checkfirst=True)
PXCLOSE1DModel.__table__.create(bind=ENGINE, checkfirst=True)
PXOPENModel.__table__.create(bind=ENGINE, checkfirst=True)
PXLOWModel.__table__.create(bind=ENGINE, checkfirst=True)
PXVOLUMEModel.__table__.create(bind=ENGINE, checkfirst=True)