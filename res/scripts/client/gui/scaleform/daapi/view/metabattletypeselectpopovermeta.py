# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/BattleTypeSelectPopoverMeta.py
from gui.Scaleform.daapi.view.lobby.popover.SmartPopOverView import SmartPopOverView

class BattleTypeSelectPopoverMeta(SmartPopOverView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends SmartPopOverView
    null
    """

    def selectFight(self, actionName):
        """
        :param actionName:
        :return :
        """
        self._printOverrideError('selectFight')

    def demoClick(self):
        """
        :return :
        """
        self._printOverrideError('demoClick')

    def getTooltipData(self, itemData):
        """
        :param itemData:
        :return String:
        """
        self._printOverrideError('getTooltipData')

    def as_updateS(self, items, isShowDemonstrator, demonstratorEnabled):
        """
        :param items:
        :param isShowDemonstrator:
        :param demonstratorEnabled:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_update(items, isShowDemonstrator, demonstratorEnabled)

    def as_setDemonstrationEnabledS(self, demonstratorEnabled):
        """
        :param demonstratorEnabled:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setDemonstrationEnabled(demonstratorEnabled)

    def as_showMiniClientInfoS(self, description, hyperlink):
        """
        :param description:
        :param hyperlink:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_showMiniClientInfo(description, hyperlink)