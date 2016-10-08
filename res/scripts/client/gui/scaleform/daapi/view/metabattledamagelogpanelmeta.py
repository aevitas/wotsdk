# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/BattleDamageLogPanelMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class BattleDamageLogPanelMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    """

    def as_showDamageLogComponentS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_showDamageLogComponent(value)

    def as_summaryStatsS(self, damage, blocked, assist):
        if self._isDAAPIInited():
            return self.flashObject.as_summaryStats(damage, blocked, assist)

    def as_updateSummaryDamageValueS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_updateSummaryDamageValue(value)

    def as_updateSummaryBlockedValueS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_updateSummaryBlockedValue(value)

    def as_updateSummaryAssistValueS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_updateSummaryAssistValue(value)

    def as_detailStatsS(self, isVisible, messages):
        if self._isDAAPIInited():
            return self.flashObject.as_detailStats(isVisible, messages)

    def as_addDetailMessageS(self, valueColor, value, actionTypeImg, vehicleTypeImg, vehicleName):
        if self._isDAAPIInited():
            return self.flashObject.as_addDetailMessage(valueColor, value, actionTypeImg, vehicleTypeImg, vehicleName)

    def as_isDownCtrlButtonS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_isDownCtrlButton(value)

    def as_isDownAltButtonS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_isDownAltButton(value)