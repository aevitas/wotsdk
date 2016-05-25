# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/AimMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIModule import BaseDAAPIModule

class AimMeta(BaseDAAPIModule):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIModule
    null
    """

    def as_initSettingsS(self, centerAlphaValue, centerType, netAlphaValue, netType, reloaderAlphaValue, reloaderType, conditionAlphaValue, conditionType, cassetteAlphaValue, cassetteType, reloaderTimerAlphaValue, reloaderTimerType):
        """
        :param centerAlphaValue:
        :param centerType:
        :param netAlphaValue:
        :param netType:
        :param reloaderAlphaValue:
        :param reloaderType:
        :param conditionAlphaValue:
        :param conditionType:
        :param cassetteAlphaValue:
        :param cassetteType:
        :param reloaderTimerAlphaValue:
        :param reloaderTimerType:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_initSettings(centerAlphaValue, centerType, netAlphaValue, netType, reloaderAlphaValue, reloaderType, conditionAlphaValue, conditionType, cassetteAlphaValue, cassetteType, reloaderTimerAlphaValue, reloaderTimerType)

    def as_recreateDeviceS(self, offsetX, offsetY):
        """
        :param offsetX:
        :param offsetY:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_recreateDevice(offsetX, offsetY)

    def as_setupReloadingCounterS(self, visible):
        """
        :param visible:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setupReloadingCounter(visible)

    def as_setReloadingS(self, duration, startTime, isReloading, currentPosition, baseTime):
        """
        :param duration:
        :param startTime:
        :param isReloading:
        :param currentPosition:
        :param baseTime:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setReloading(duration, startTime, isReloading, currentPosition, baseTime)

    def as_setReloadingAsPercentS(self, percent, isReloading):
        """
        :param percent:
        :param isReloading:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setReloadingAsPercent(percent, isReloading)

    def as_correctReloadingTimeS(self, time):
        """
        :param time:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_correctReloadingTime(time)

    def as_setReloadingTimeWithCorrectionS(self, duration, startTime, remainingTime):
        """
        :param duration:
        :param startTime:
        :param remainingTime:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setReloadingTimeWithCorrection(duration, startTime, remainingTime)

    def as_setHealthS(self, percent):
        """
        :param percent:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setHealth(percent)

    def as_setAmmoStockS(self, quantity, quantityInClip, isLow, clipState, clipReloaded):
        """
        :param quantity:
        :param quantityInClip:
        :param isLow:
        :param clipState:
        :param clipReloaded:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setAmmoStock(quantity, quantityInClip, isLow, clipState, clipReloaded)

    def as_setClipParamsS(self, clipCapacity, burst):
        """
        :param clipCapacity:
        :param burst:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setClipParams(clipCapacity, burst)

    def as_setTargetS(self, name, type, color):
        """
        :param name:
        :param type:
        :param color:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setTarget(name, type, color)

    def as_clearTargetS(self, startTime):
        """
        :param startTime:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_clearTarget(startTime)

    def as_updateTargetS(self, dist):
        """
        :param dist:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_updateTarget(dist)

    def as_updatePlayerInfoS(self, info):
        """
        :param info:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_updatePlayerInfo(info)

    def as_updateAmmoStateS(self, hasAmmo):
        """
        :param hasAmmo:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_updateAmmoState(hasAmmo)

    def as_updateAmmoInfoPosS(self):
        """
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_updateAmmoInfoPos()

    def as_updateAdjustS(self, brightness, contrast, saturation, hue):
        """
        :param brightness:
        :param contrast:
        :param saturation:
        :param hue:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_updateAdjust(brightness, contrast, saturation, hue)

    def as_updateDistanceS(self, dist):
        """
        :param dist:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_updateDistance(dist)

    def as_updateReloadingBaseTimeS(self, baseTime, isReloaded):
        """
        :param baseTime:
        :param isReloaded:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_updateReloadingBaseTime(baseTime, isReloaded)

    def as_clearPreviousCorrectionS(self):
        """
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_clearPreviousCorrection()