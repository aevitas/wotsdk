# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/SendInvitesWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class SendInvitesWindowMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    null
    """

    def showError(self, value):
        """
        :param value:
        :return :
        """
        self._printOverrideError('showError')

    def setOnlineFlag(self, value):
        """
        :param value:
        :return :
        """
        self._printOverrideError('setOnlineFlag')

    def sendInvites(self, accountsToInvite, comment):
        """
        :param accountsToInvite:
        :param comment:
        :return :
        """
        self._printOverrideError('sendInvites')

    def getAllAvailableContacts(self):
        """
        :return Array:
        """
        self._printOverrideError('getAllAvailableContacts')

    def as_onReceiveSendInvitesCooldownS(self, value):
        """
        :param value:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_onReceiveSendInvitesCooldown(value)

    def as_setDefaultOnlineFlagS(self, onlineFlag):
        """
        :param onlineFlag:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setDefaultOnlineFlag(onlineFlag)

    def as_setInvalidUserTagsS(self, tags):
        """
        :param tags:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setInvalidUserTags(tags)

    def as_setWindowTitleS(self, value):
        """
        :param value:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setWindowTitle(value)

    def as_onContactUpdatedS(self, contact):
        """
        :param contact:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_onContactUpdated(contact)

    def as_onListStateChangedS(self, isEmpty):
        """
        :param isEmpty:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_onListStateChanged(isEmpty)

    def as_enableDescriptionS(self, isEnabled):
        """
        :param isEnabled:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_enableDescription(isEnabled)

    def as_enableMassSendS(self, isEnabled, addAllTooltip):
        """
        :param isEnabled:
        :param addAllTooltip:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_enableMassSend(isEnabled, addAllTooltip)