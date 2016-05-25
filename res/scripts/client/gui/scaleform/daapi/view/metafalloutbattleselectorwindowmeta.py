# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/FalloutBattleSelectorWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class FalloutBattleSelectorWindowMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    null
    """

    def onDominationBtnClick(self):
        """
        :return :
        """
        self._printOverrideError('onDominationBtnClick')

    def onMultiteamBtnClick(self):
        """
        :return :
        """
        self._printOverrideError('onMultiteamBtnClick')

    def onSelectCheckBoxAutoSquad(self, isSelected):
        """
        :param isSelected:
        :return :
        """
        self._printOverrideError('onSelectCheckBoxAutoSquad')

    def getClientID(self):
        """
        :return Number:
        """
        self._printOverrideError('getClientID')

    def as_setInitDataS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setInitData(data)

    def as_setBtnStatesS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setBtnStates(data)

    def as_setTooltipsS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setTooltips(data)