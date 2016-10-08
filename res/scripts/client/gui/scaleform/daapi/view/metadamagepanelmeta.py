# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/DamagePanelMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class DamagePanelMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    """

    def clickToTankmanIcon(self, entityName):
        self._printOverrideError('clickToTankmanIcon')

    def clickToDeviceIcon(self, entityName):
        self._printOverrideError('clickToDeviceIcon')

    def clickToFireIcon(self):
        self._printOverrideError('clickToFireIcon')

    def getTooltipData(self, entityName, state):
        self._printOverrideError('getTooltipData')

    def as_setPlayerInfoS(self, playerName, clanName, regionName, vehicleTypeName):
        if self._isDAAPIInited():
            return self.flashObject.as_setPlayerInfo(playerName, clanName, regionName, vehicleTypeName)

    def as_setupS(self, healthStr, progress, indicatorType, crewLayout, yawLimits, hasTurretRotator, isAutoRotationOn):
        if self._isDAAPIInited():
            return self.flashObject.as_setup(healthStr, progress, indicatorType, crewLayout, yawLimits, hasTurretRotator, isAutoRotationOn)

    def as_updateHealthS(self, healthStr, progress):
        if self._isDAAPIInited():
            return self.flashObject.as_updateHealth(healthStr, progress)

    def as_updateSpeedS(self, speed):
        if self._isDAAPIInited():
            return self.flashObject.as_updateSpeed(speed)

    def as_setMaxSpeedS(self, maxSpeed):
        if self._isDAAPIInited():
            return self.flashObject.as_setMaxSpeed(maxSpeed)

    def as_setRpmVibrationS(self, intensity):
        if self._isDAAPIInited():
            return self.flashObject.as_setRpmVibration(intensity)

    def as_playEngineStartAnimS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_playEngineStartAnim()

    def as_startVehicleStartAnimS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_startVehicleStartAnim()

    def as_finishVehicleStartAnimS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_finishVehicleStartAnim()

    def as_setNormalizedEngineRpmS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setNormalizedEngineRpm(value)

    def as_setCruiseModeS(self, mode):
        if self._isDAAPIInited():
            return self.flashObject.as_setCruiseMode(mode)

    def as_setAutoRotationS(self, isOn):
        if self._isDAAPIInited():
            return self.flashObject.as_setAutoRotation(isOn)

    def as_updateDeviceStateS(self, deviceName, deviceState):
        if self._isDAAPIInited():
            return self.flashObject.as_updateDeviceState(deviceName, deviceState)

    def as_updateRepairingDeviceS(self, deviceName, percents, seconds):
        if self._isDAAPIInited():
            return self.flashObject.as_updateRepairingDevice(deviceName, percents, seconds)

    def as_setVehicleDestroyedS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_setVehicleDestroyed()

    def as_setCrewDeactivatedS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_setCrewDeactivated()

    def as_showS(self, isShow):
        if self._isDAAPIInited():
            return self.flashObject.as_show(isShow)

    def as_setFireInVehicleS(self, isInFire):
        if self._isDAAPIInited():
            return self.flashObject.as_setFireInVehicle(isInFire)

    def as_setStaticDataS(self, fireMsg):
        if self._isDAAPIInited():
            return self.flashObject.as_setStaticData(fireMsg)

    def as_resetS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_reset()

    def as_setPlaybackSpeedS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setPlaybackSpeed(value)