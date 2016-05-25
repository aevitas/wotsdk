# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/BattleSessionWindowMeta.py
from gui.Scaleform.daapi.view.lobby.prb_windows.PrebattleWindow import PrebattleWindow

class BattleSessionWindowMeta(PrebattleWindow):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends PrebattleWindow
    null
    """

    def requestToAssignMember(self, accId):
        """
        :param accId:
        :return :
        """
        self._printOverrideError('requestToAssignMember')

    def requestToUnassignMember(self, accId):
        """
        :param accId:
        :return :
        """
        self._printOverrideError('requestToUnassignMember')

    def canMoveToAssigned(self):
        """
        :return Boolean:
        """
        self._printOverrideError('canMoveToAssigned')

    def canMoveToUnassigned(self):
        """
        :return Boolean:
        """
        self._printOverrideError('canMoveToUnassigned')

    def as_setStartTimeS(self, value):
        """
        :param value:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setStartTime(value)

    def as_setTotalPlayersCountS(self, value):
        """
        :param value:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setTotalPlayersCount(value)

    def as_setInfoS(self, wins, map, firstTeam, secondTeam, count, description, comment):
        """
        :param wins:
        :param map:
        :param firstTeam:
        :param secondTeam:
        :param count:
        :param description:
        :param comment:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setInfo(wins, map, firstTeam, secondTeam, count, description, comment)

    def as_setNationsLimitsS(self, nations):
        """
        :param nations:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setNationsLimits(nations)

    def as_setClassesLimitsS(self, vehicleLevels, classesLimitsAreIdentical):
        """
        :param vehicleLevels:
        :param classesLimitsAreIdentical:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setClassesLimits(vehicleLevels, classesLimitsAreIdentical)

    def as_setCommonLimitsS(self, teamLevel, maxPlayers):
        """
        :param teamLevel:
        :param maxPlayers:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setCommonLimits(teamLevel, maxPlayers)

    def as_setPlayersCountTextS(self, playersCountText):
        """
        :param playersCountText:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setPlayersCountText(playersCountText)