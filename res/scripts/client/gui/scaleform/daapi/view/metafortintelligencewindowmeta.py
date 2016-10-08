# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/FortIntelligenceWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class FortIntelligenceWindowMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    """

    def requestClanFortInfo(self, index):
        self._printOverrideError('requestClanFortInfo')

    def as_setStatusTextS(self, statusText):
        if self._isDAAPIInited():
            return self.flashObject.as_setStatusText(statusText)

    def as_getSearchDPS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_getSearchDP()

    def as_getCurrentListIndexS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_getCurrentListIndex()

    def as_selectByIndexS(self, index):
        if self._isDAAPIInited():
            return self.flashObject.as_selectByIndex(index)

    def as_setTableHeaderS(self, data):
        """
        :param data: Represented by NormalSortingTableHeaderVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setTableHeader(data)