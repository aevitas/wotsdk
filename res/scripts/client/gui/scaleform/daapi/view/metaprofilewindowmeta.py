# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/ProfileWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class ProfileWindowMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    null
    """

    def userAddFriend(self):
        """
        :return :
        """
        self._printOverrideError('userAddFriend')

    def userAddToClan(self):
        """
        :return :
        """
        self._printOverrideError('userAddToClan')

    def userSetIgnored(self):
        """
        :return :
        """
        self._printOverrideError('userSetIgnored')

    def userCreatePrivateChannel(self):
        """
        :return :
        """
        self._printOverrideError('userCreatePrivateChannel')

    def as_setInitDataS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setInitData(data)

    def as_addFriendAvailableS(self, value):
        """
        :param value:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_addFriendAvailable(value)

    def as_addToClanAvailableS(self, value):
        """
        :param value:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_addToClanAvailable(value)

    def as_addToClanVisibleS(self, value):
        """
        :param value:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_addToClanVisible(value)

    def as_setIgnoredAvailableS(self, value):
        """
        :param value:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setIgnoredAvailable(value)

    def as_setCreateChannelAvailableS(self, value):
        """
        :param value:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setCreateChannelAvailable(value)