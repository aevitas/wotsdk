# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/FortBuildingCardPopoverMeta.py
from gui.Scaleform.daapi.view.lobby.popover.SmartPopOverView import SmartPopOverView

class FortBuildingCardPopoverMeta(SmartPopOverView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends SmartPopOverView
    null
    """

    def openUpgradeWindow(self, value):
        """
        :param value:
        :return :
        """
        self._printOverrideError('openUpgradeWindow')

    def openAssignedPlayersWindow(self, value):
        """
        :param value:
        :return :
        """
        self._printOverrideError('openAssignedPlayersWindow')

    def openDemountBuildingWindow(self, value):
        """
        :param value:
        :return :
        """
        self._printOverrideError('openDemountBuildingWindow')

    def openDirectionControlWindow(self):
        """
        :return :
        """
        self._printOverrideError('openDirectionControlWindow')

    def openBuyOrderWindow(self):
        """
        :return :
        """
        self._printOverrideError('openBuyOrderWindow')

    def as_setDataS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)

    def as_setModernizationDestructionEnablingS(self, modernizationButtonEnabled, destroyButtonEnabled, modernizationButtonTooltip, destroyButtonTooltip):
        """
        :param modernizationButtonEnabled:
        :param destroyButtonEnabled:
        :param modernizationButtonTooltip:
        :param destroyButtonTooltip:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setModernizationDestructionEnabling(modernizationButtonEnabled, destroyButtonEnabled, modernizationButtonTooltip, destroyButtonTooltip)