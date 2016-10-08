# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/FalloutBattleSelectorWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class FalloutBattleSelectorWindowMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    """

    def onDominationBtnClick(self):
        self._printOverrideError('onDominationBtnClick')

    def onMultiteamBtnClick(self):
        self._printOverrideError('onMultiteamBtnClick')

    def onSelectCheckBoxAutoSquad(self, isSelected):
        self._printOverrideError('onSelectCheckBoxAutoSquad')

    def getClientID(self):
        self._printOverrideError('getClientID')

    def as_setInitDataS(self, data):
        """
        :param data: Represented by SelectorWindowStaticDataVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setInitData(data)

    def as_setBtnStatesS(self, data):
        """
        :param data: Represented by SelectorWindowBtnStatesVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setBtnStates(data)

    def as_setTooltipsS(self, data):
        """
        :param data: Represented by FalloutBattleSelectorTooltipVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setTooltips(data)