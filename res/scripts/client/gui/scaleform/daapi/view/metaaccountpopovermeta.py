# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/AccountPopoverMeta.py
from gui.Scaleform.daapi.view.lobby.popover.SmartPopOverView import SmartPopOverView

class AccountPopoverMeta(SmartPopOverView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends SmartPopOverView
    """

    def openBoostersWindow(self, slotId):
        self._printOverrideError('openBoostersWindow')

    def openClanResearch(self):
        self._printOverrideError('openClanResearch')

    def openRequestWindow(self):
        self._printOverrideError('openRequestWindow')

    def openInviteWindow(self):
        self._printOverrideError('openInviteWindow')

    def openClanStatistic(self):
        self._printOverrideError('openClanStatistic')

    def openCrewStatistic(self):
        self._printOverrideError('openCrewStatistic')

    def openReferralManagement(self):
        self._printOverrideError('openReferralManagement')

    def as_setDataS(self, data):
        """
        :param data: Represented by AccountPopoverMainVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)

    def as_setClanDataS(self, data):
        """
        :param data: Represented by AccountClanPopoverBlockVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setClanData(data)

    def as_setCrewDataS(self, data):
        """
        :param data: Represented by AccountPopoverBlockVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setCrewData(data)

    def as_setClanEmblemS(self, emblemId):
        if self._isDAAPIInited():
            return self.flashObject.as_setClanEmblem(emblemId)

    def as_setCrewEmblemS(self, emblemId):
        if self._isDAAPIInited():
            return self.flashObject.as_setCrewEmblem(emblemId)

    def as_setReferralDataS(self, data):
        """
        :param data: Represented by AccountPopoverReferralBlockVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setReferralData(data)