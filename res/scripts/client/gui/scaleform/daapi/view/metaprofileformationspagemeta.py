# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/ProfileFormationsPageMeta.py
from gui.Scaleform.daapi.view.lobby.profile.ProfileSection import ProfileSection

class ProfileFormationsPageMeta(ProfileSection):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends ProfileSection
    null
    """

    def showFort(self):
        """
        :return :
        """
        self._printOverrideError('showFort')

    def searchStaticTeams(self):
        """
        :return :
        """
        self._printOverrideError('searchStaticTeams')

    def createFort(self):
        """
        :return :
        """
        self._printOverrideError('createFort')

    def showTeam(self, teamId):
        """
        :param teamId:
        :return :
        """
        self._printOverrideError('showTeam')

    def onClanLinkNavigate(self, code):
        """
        :param code:
        :return :
        """
        self._printOverrideError('onClanLinkNavigate')

    def as_setClanInfoS(self, clanInfo):
        """
        :param clanInfo:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setClanInfo(clanInfo)

    def as_setClubInfoS(self, clubInfo):
        """
        :param clubInfo:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setClubInfo(clubInfo)

    def as_setFortInfoS(self, fortInfo):
        """
        :param fortInfo:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setFortInfo(fortInfo)

    def as_setClubHistoryS(self, history):
        """
        :param history:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setClubHistory(history)

    def as_setClanEmblemS(self, clanIcon):
        """
        :param clanIcon:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setClanEmblem(clanIcon)

    def as_setClubEmblemS(self, clubIcon):
        """
        :param clubIcon:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setClubEmblem(clubIcon)