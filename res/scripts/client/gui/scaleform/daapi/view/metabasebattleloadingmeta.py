# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/BaseBattleLoadingMeta.py
from gui.Scaleform.framework.entities.View import View

class BaseBattleLoadingMeta(View):

    def as_setProgressS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setProgress(value)

    def as_setTipS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setTip(value)

    def as_setTipTitleS(self, title):
        if self._isDAAPIInited():
            return self.flashObject.as_setTipTitle(title)

    def as_setEventInfoPanelDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setEventInfoPanelData(data)

    def as_setArenaInfoS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setArenaInfo(data)

    def as_setMapIconS(self, source):
        if self._isDAAPIInited():
            return self.flashObject.as_setMapIcon(source)

    def as_setVisualTipInfoS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setVisualTipInfo(data)

    def as_setPlayerDataS(self, playerVehicleID, prebattleID):
        if self._isDAAPIInited():
            return self.flashObject.as_setPlayerData(playerVehicleID, prebattleID)

    def as_setVehiclesDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setVehiclesData(data)

    def as_addVehicleInfoS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_addVehicleInfo(data)

    def as_updateVehicleInfoS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_updateVehicleInfo(data)

    def as_setVehicleStatusS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setVehicleStatus(data)

    def as_setPlayerStatusS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setPlayerStatus(data)