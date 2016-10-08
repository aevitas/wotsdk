# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/FortClanBattleRoomMeta.py
from gui.Scaleform.daapi.view.lobby.rally.BaseRallyRoomView import BaseRallyRoomView

class FortClanBattleRoomMeta(BaseRallyRoomView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseRallyRoomView
    """

    def onTimerAlert(self):
        self._printOverrideError('onTimerAlert')

    def as_updateTeamHeaderTextS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_updateTeamHeaderText(value)

    def as_setBattleRoomDataS(self, data):
        """
        :param data: Represented by FortClanBattleRoomVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setBattleRoomData(data)

    def as_updateReadyStatusS(self, mineValue, enemyValue):
        if self._isDAAPIInited():
            return self.flashObject.as_updateReadyStatus(mineValue, enemyValue)

    def as_setTimerDeltaS(self, data):
        """
        :param data: Represented by ClanBattleTimerVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setTimerDelta(data)

    def as_updateDirectionsS(self, data):
        """
        :param data: Represented by ConnectedDirectionsVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_updateDirections(data)

    def as_setMineClanIconS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setMineClanIcon(value)

    def as_setEnemyClanIconS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setEnemyClanIcon(value)