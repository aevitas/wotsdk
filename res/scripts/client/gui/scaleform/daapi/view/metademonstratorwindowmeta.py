# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/DemonstratorWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class DemonstratorWindowMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    """

    def onMapSelected(self, mapID):
        self._printOverrideError('onMapSelected')

    def as_setDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)