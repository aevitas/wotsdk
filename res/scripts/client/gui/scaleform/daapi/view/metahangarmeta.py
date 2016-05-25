# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/HangarMeta.py
from gui.Scaleform.framework.entities.View import View

class HangarMeta(View):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends View
    null
    """

    def onEscape(self):
        """
        :return :
        """
        self._printOverrideError('onEscape')

    def showHelpLayout(self):
        """
        :return :
        """
        self._printOverrideError('showHelpLayout')

    def closeHelpLayout(self):
        """
        :return :
        """
        self._printOverrideError('closeHelpLayout')

    def toggleGUIEditor(self):
        """
        :return :
        """
        self._printOverrideError('toggleGUIEditor')

    def as_setCrewEnabledS(self, value):
        """
        :param value:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setCrewEnabled(value)

    def as_setCarouselEnabledS(self, value):
        """
        :param value:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setCarouselEnabled(value)

    def as_setupAmmunitionPanelS(self, maintenanceEnabled, maintenanceTooltip, customizationEnabled, customizationTooltip):
        """
        :param maintenanceEnabled:
        :param maintenanceTooltip:
        :param customizationEnabled:
        :param customizationTooltip:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setupAmmunitionPanel(maintenanceEnabled, maintenanceTooltip, customizationEnabled, customizationTooltip)

    def as_setControlsVisibleS(self, value):
        """
        :param value:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setControlsVisible(value)

    def as_setVisibleS(self, value):
        """
        :param value:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setVisible(value)

    def as_showHelpLayoutS(self):
        """
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_showHelpLayout()

    def as_closeHelpLayoutS(self):
        """
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_closeHelpLayout()

    def as_setIsIGRS(self, value, text):
        """
        :param value:
        :param text:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setIsIGR(value, text)

    def as_setServerStatsS(self, stats, tooltipType):
        """
        :param stats:
        :param tooltipType:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setServerStats(stats, tooltipType)

    def as_setServerStatsInfoS(self, tooltipFullData):
        """
        :param tooltipFullData:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setServerStatsInfo(tooltipFullData)

    def as_setVehicleIGRS(self, actionIgrDaysLeft):
        """
        :param actionIgrDaysLeft:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setVehicleIGR(actionIgrDaysLeft)

    def as_showMiniClientInfoS(self, description, hyperlink):
        """
        :param description:
        :param hyperlink:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_showMiniClientInfo(description, hyperlink)

    def as_show3DSceneTooltipS(self, id, args):
        """
        :param id:
        :param args:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_show3DSceneTooltip(id, args)

    def as_hide3DSceneTooltipS(self):
        """
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_hide3DSceneTooltip()