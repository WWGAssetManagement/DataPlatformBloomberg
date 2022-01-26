from config.settings import ENGINE
from bloomberg.model.models import(
    INDXMEMBERSModel, 
    PXCLOSE1DModel,
    PXOPENModel,
    PXLOWModel,
    PXVOLUMEModel,
    PXHIGHModel,
    DelistModel,
    ERNANNDTANDPERModel,
    GICSSectorNameModel,
    GICSINDUSTRYNAMEModel,
    GICSSectorModel,
    GICSIndustryModel,
)


INDXMEMBERSModel.__table__.create(bind=ENGINE, checkfirst=True)
PXCLOSE1DModel.__table__.create(bind=ENGINE, checkfirst=True)
PXOPENModel.__table__.create(bind=ENGINE, checkfirst=True)
PXLOWModel.__table__.create(bind=ENGINE, checkfirst=True)
PXVOLUMEModel.__table__.create(bind=ENGINE, checkfirst=True)
PXHIGHModel.__table__.create(bind=ENGINE, checkfirst=True)
DelistModel.__table__.create(bind=ENGINE, checkfirst=True)
ERNANNDTANDPERModel.__table__.create(bind=ENGINE, checkfirst=True)
GICSSectorNameModel.__table__.create(bind=ENGINE, checkfirst=True)
GICSINDUSTRYNAMEModel.__table__.create(bind=ENGINE, checkfirst=True)
GICSSectorModel.__table__.create(bind=ENGINE, checkfirst=True)
GICSIndustryModel.__table__.create(bind=ENGINE, checkfirst=True)