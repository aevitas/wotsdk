# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/PrebattleWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class PrebattleWindowMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    null
    """

    def requestToReady(self, value):
        """
        :param value:
        :return :
        """
        self._printOverrideError('requestToReady')

    def requestToLeave(self):
        """
        :return :
        """
        self._printOverrideError('requestToLeave')

    def showPrebattleSendInvitesWindow(self):
        """
        :return :
        """
        self._printOverrideError('showPrebattleSendInvitesWindow')

    def showFAQWindow(self):
        """
        :return :
        """
        self._printOverrideError('showFAQWindow')

    def canSendInvite(self):
        """
        :return Boolean:
        """
        self._printOverrideError('canSendInvite')

    def canKickPlayer(self):
        """
        :return Boolean:
        """
        self._printOverrideError('canKickPlayer')

    def isPlayerReady(self):
        """
        :return Boolean:
        """
        self._printOverrideError('isPlayerReady')

    def isPlayerCreator(self):
        """
        :return Boolean:
        """
        self._printOverrideError('isPlayerCreator')

    def isReadyBtnEnabled(self):
        """
        :return Boolean:
        """
        self._printOverrideError('isReadyBtnEnabled')

    def isLeaveBtnEnabled(self):
        """
        :return Boolean:
        """
        self._printOverrideError('isLeaveBtnEnabled')

    def getClientID(self):
        """
        :return Number:
        """
        self._printOverrideError('getClientID')

    def as_setRosterListS(self, team, assigned, rosters):
        """
        :param team:
        :param assigned:
        :param rosters:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setRosterList(team, assigned, rosters)

    def as_setPlayerStateS(self, team, assigned, data):
        """
        :param team:
        :param assigned:
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setPlayerState(team, assigned, data)

    def as_enableLeaveBtnS(self, value):
        """
        :param value:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_enableLeaveBtn(value)

    def as_enableReadyBtnS(self, value):
        """
        :param value:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_enableReadyBtn(value)

    def as_setCoolDownForReadyButtonS(self, value):
        """
        :param value:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setCoolDownForReadyButton(value)

    def as_resetReadyButtonCoolDownS(self):
        """
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_resetReadyButtonCoolDown()

    def as_toggleReadyBtnS(self, value):
        """
        :param value:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_toggleReadyBtn(value)

    def as_refreshPermissionsS(self):
        """
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_refreshPermissions()