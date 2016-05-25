# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/FortListMeta.py
from gui.Scaleform.daapi.view.lobby.rally.BaseRallyListView import BaseRallyListView

class FortListMeta(BaseRallyListView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseRallyListView
    null
    """

    def changeDivisionIndex(self, index):
        """
        :param index:
        :return :
        """
        self._printOverrideError('changeDivisionIndex')

    def as_getDivisionsDPS(self):
        """
        :return Object:
        """
        if self._isDAAPIInited():
            return self.flashObject.as_getDivisionsDP()

    def as_setSelectedDivisionS(self, index):
        """
        :param index:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setSelectedDivision(index)

    def as_setCreationEnabledS(self, value):
        """
        :param value:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setCreationEnabled(value)

    def as_setRegulationInfoS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setRegulationInfo(data)

    def as_setTableHeaderS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setTableHeader(data)

    def as_tryShowTextMessageS(self):
        """
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_tryShowTextMessage()

    def as_setCurfewEnabledS(self, showWarning):
        """
        :param showWarning:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setCurfewEnabled(showWarning)