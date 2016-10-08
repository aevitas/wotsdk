# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/CrosshairPanelMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class CrosshairPanelMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    """

    def as_populateS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_populate()

    def as_disposeS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_dispose()

    def as_setSettingsS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setSettings(data)

    def as_setViewS(self, view):
        if self._isDAAPIInited():
            return self.flashObject.as_setView(view)

    def as_recreateDeviceS(self, offsetX, offsetY):
        if self._isDAAPIInited():
            return self.flashObject.as_recreateDevice(offsetX, offsetY)

    def as_setReloadingCounterShownS(self, visible):
        if self._isDAAPIInited():
            return self.flashObject.as_setReloadingCounterShown(visible)

    def as_setReloadingS(self, duration, baseTime, startTime, isReloading):
        if self._isDAAPIInited():
            return self.flashObject.as_setReloading(duration, baseTime, startTime, isReloading)

    def as_setReloadingAsPercentS(self, percent, isReloading):
        if self._isDAAPIInited():
            return self.flashObject.as_setReloadingAsPercent(percent, isReloading)

    def as_setHealthS(self, percent):
        if self._isDAAPIInited():
            return self.flashObject.as_setHealth(percent)

    def as_setAmmoStockS(self, quantity, quantityInClip, isLow, clipState, clipReloaded):
        if self._isDAAPIInited():
            return self.flashObject.as_setAmmoStock(quantity, quantityInClip, isLow, clipState, clipReloaded)

    def as_setClipParamsS(self, clipCapacity, burst):
        if self._isDAAPIInited():
            return self.flashObject.as_setClipParams(clipCapacity, burst)

    def as_setDistanceS(self, dist):
        if self._isDAAPIInited():
            return self.flashObject.as_setDistance(dist)

    def as_clearDistanceS(self, immediate):
        if self._isDAAPIInited():
            return self.flashObject.as_clearDistance(immediate)

    def as_updatePlayerInfoS(self, info):
        if self._isDAAPIInited():
            return self.flashObject.as_updatePlayerInfo(info)

    def as_updateAmmoStateS(self, ammoState):
        if self._isDAAPIInited():
            return self.flashObject.as_updateAmmoState(ammoState)

    def as_setZoomS(self, zoomStr):
        if self._isDAAPIInited():
            return self.flashObject.as_setZoom(zoomStr)