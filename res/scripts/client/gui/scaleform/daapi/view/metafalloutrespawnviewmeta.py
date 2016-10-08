# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/FalloutRespawnViewMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class FalloutRespawnViewMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    """

    def onVehicleSelected(self, vehicleID):
        self._printOverrideError('onVehicleSelected')

    def onPostmortemBtnClick(self):
        self._printOverrideError('onPostmortemBtnClick')

    def as_initializeS(self, mainData, slotsData):
        if self._isDAAPIInited():
            return self.flashObject.as_initialize(mainData, slotsData)

    def as_updateTimerS(self, mainTimer, slotsStateData):
        if self._isDAAPIInited():
            return self.flashObject.as_updateTimer(mainTimer, slotsStateData)

    def as_updateS(self, selectedVehicleName, slotsStateData):
        if self._isDAAPIInited():
            return self.flashObject.as_update(selectedVehicleName, slotsStateData)

    def as_showGasAttackModeS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_showGasAttackMode()