# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/AccountPopoverMeta.py
from gui.Scaleform.daapi.view.lobby.popover.SmartPopOverView import SmartPopOverView

class AccountPopoverMeta(SmartPopOverView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends SmartPopOverView
    null
    """

    def openBoostersWindow(self, slotId):
        """
        :param slotId:
        :return :
        """
        self._printOverrideError('openBoostersWindow')

    def openClanResearch(self):
        """
        :return :
        """
        self._printOverrideError('openClanResearch')

    def openRequestWindow(self):
        """
        :return :
        """
        self._printOverrideError('openRequestWindow')

    def openInviteWindow(self):
        """
        :return :
        """
        self._printOverrideError('openInviteWindow')

    def openClanStatistic(self):
        """
        :return :
        """
        self._printOverrideError('openClanStatistic')

    def openCrewStatistic(self):
        """
        :return :
        """
        self._printOverrideError('openCrewStatistic')

    def openReferralManagement(self):
        """
        :return :
        """
        self._printOverrideError('openReferralManagement')

    def as_setDataS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)

    def as_setClanDataS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setClanData(data)

    def as_setCrewDataS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setCrewData(data)

    def as_setClanEmblemS(self, emblemId):
        """
        :param emblemId:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setClanEmblem(emblemId)

    def as_setCrewEmblemS(self, emblemId):
        """
        :param emblemId:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setCrewEmblem(emblemId)

    def as_setReferralDataS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setReferralData(data)