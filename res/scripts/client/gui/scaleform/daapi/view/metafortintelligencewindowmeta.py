# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/FortIntelligenceWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class FortIntelligenceWindowMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    null
    """

    def requestClanFortInfo(self, index):
        """
        :param index:
        :return :
        """
        self._printOverrideError('requestClanFortInfo')

    def as_setStatusTextS(self, statusText):
        """
        :param statusText:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setStatusText(statusText)

    def as_getSearchDPS(self):
        """
        :return Object:
        """
        if self._isDAAPIInited():
            return self.flashObject.as_getSearchDP()

    def as_getCurrentListIndexS(self):
        """
        :return int:
        """
        if self._isDAAPIInited():
            return self.flashObject.as_getCurrentListIndex()

    def as_selectByIndexS(self, index):
        """
        :param index:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_selectByIndex(index)

    def as_setTableHeaderS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setTableHeader(data)