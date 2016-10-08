# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/ServerStatsMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class ServerStatsMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    """

    def relogin(self, id):
        self._printOverrideError('relogin')

    def startListenCsisUpdate(self, startListenCsis):
        self._printOverrideError('startListenCsisUpdate')

    def as_changePeripheryFailedS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_changePeripheryFailed()

    def as_disableRoamingDDS(self, disable):
        if self._isDAAPIInited():
            return self.flashObject.as_disableRoamingDD(disable)

    def as_setServerStatsS(self, stats, tooltipType):
        if self._isDAAPIInited():
            return self.flashObject.as_setServerStats(stats, tooltipType)

    def as_setServerStatsInfoS(self, tooltipFullData):
        if self._isDAAPIInited():
            return self.flashObject.as_setServerStatsInfo(tooltipFullData)

    def as_getServersDPS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_getServersDP()

    def as_setSelectedServerIndexS(self, index):
        if self._isDAAPIInited():
            return self.flashObject.as_setSelectedServerIndex(index)