# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/AimMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIModule import BaseDAAPIModule

class AimMeta(BaseDAAPIModule):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIModule
    """

    def as_initSettingsS(self, centerAlphaValue, centerType, netAlphaValue, netType, reloaderAlphaValue, reloaderType, conditionAlphaValue, conditionType, cassetteAlphaValue, cassetteType, reloaderTimerAlphaValue, reloaderTimerType):
        if self._isDAAPIInited():
            return self.flashObject.as_initSettings(centerAlphaValue, centerType, netAlphaValue, netType, reloaderAlphaValue, reloaderType, conditionAlphaValue, conditionType, cassetteAlphaValue, cassetteType, reloaderTimerAlphaValue, reloaderTimerType)

    def as_recreateDeviceS(self, offsetX, offsetY):
        if self._isDAAPIInited():
            return self.flashObject.as_recreateDevice(offsetX, offsetY)

    def as_setupReloadingCounterS(self, visible):
        if self._isDAAPIInited():
            return self.flashObject.as_setupReloadingCounter(visible)

    def as_setReloadingS(self, duration, startTime, isReloading, currentPosition, baseTime):
        if self._isDAAPIInited():
            return self.flashObject.as_setReloading(duration, startTime, isReloading, currentPosition, baseTime)

    def as_setReloadingAsPercentS(self, percent, isReloading):
        if self._isDAAPIInited():
            return self.flashObject.as_setReloadingAsPercent(percent, isReloading)

    def as_correctReloadingTimeS(self, time):
        if self._isDAAPIInited():
            return self.flashObject.as_correctReloadingTime(time)

    def as_setReloadingTimeWithCorrectionS(self, duration, startTime, remainingTime):
        if self._isDAAPIInited():
            return self.flashObject.as_setReloadingTimeWithCorrection(duration, startTime, remainingTime)

    def as_setHealthS(self, percent):
        if self._isDAAPIInited():
            return self.flashObject.as_setHealth(percent)

    def as_setAmmoStockS(self, quantity, quantityInClip, isLow, clipState, clipReloaded):
        if self._isDAAPIInited():
            return self.flashObject.as_setAmmoStock(quantity, quantityInClip, isLow, clipState, clipReloaded)

    def as_setClipParamsS(self, clipCapacity, burst):
        if self._isDAAPIInited():
            return self.flashObject.as_setClipParams(clipCapacity, burst)

    def as_setTargetS(self, name, type, color):
        if self._isDAAPIInited():
            return self.flashObject.as_setTarget(name, type, color)

    def as_clearTargetS(self, startTime):
        if self._isDAAPIInited():
            return self.flashObject.as_clearTarget(startTime)

    def as_updateTargetS(self, dist):
        if self._isDAAPIInited():
            return self.flashObject.as_updateTarget(dist)

    def as_updatePlayerInfoS(self, info):
        if self._isDAAPIInited():
            return self.flashObject.as_updatePlayerInfo(info)

    def as_updateAmmoStateS(self, hasAmmo):
        if self._isDAAPIInited():
            return self.flashObject.as_updateAmmoState(hasAmmo)

    def as_updateAmmoInfoPosS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_updateAmmoInfoPos()

    def as_updateAdjustS(self, brightness, contrast, saturation, hue):
        if self._isDAAPIInited():
            return self.flashObject.as_updateAdjust(brightness, contrast, saturation, hue)

    def as_updateDistanceS(self, dist):
        if self._isDAAPIInited():
            return self.flashObject.as_updateDistance(dist)

    def as_updateReloadingBaseTimeS(self, baseTime, isReloaded):
        if self._isDAAPIInited():
            return self.flashObject.as_updateReloadingBaseTime(baseTime, isReloaded)

    def as_clearPreviousCorrectionS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_clearPreviousCorrection()

    def as_setZoomS(self, zoomStr):
        if self._isDAAPIInited():
            return self.flashObject.as_setZoom(zoomStr)