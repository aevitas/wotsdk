# Embedded file name: scripts/client/messenger/gui/Scaleform/meta/ContactsWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class ContactsWindowMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    null
    """

    def searchContact(self, criteria):
        """
        :param criteria:
        :return :
        """
        self._printOverrideError('searchContact')

    def addToFriends(self, uid, name):
        """
        :param uid:
        :param name:
        :return :
        """
        self._printOverrideError('addToFriends')

    def addToIgnored(self, uid, name):
        """
        :param uid:
        :param name:
        :return :
        """
        self._printOverrideError('addToIgnored')

    def isEnabledInRoaming(self, uid):
        """
        :param uid:
        :return Boolean:
        """
        self._printOverrideError('isEnabledInRoaming')

    def as_getFriendsDPS(self):
        """
        :return Object:
        """
        if self._isDAAPIInited():
            return self.flashObject.as_getFriendsDP()

    def as_getClanDPS(self):
        """
        :return Object:
        """
        if self._isDAAPIInited():
            return self.flashObject.as_getClanDP()

    def as_getIgnoredDPS(self):
        """
        :return Object:
        """
        if self._isDAAPIInited():
            return self.flashObject.as_getIgnoredDP()

    def as_getMutedDPS(self):
        """
        :return Object:
        """
        if self._isDAAPIInited():
            return self.flashObject.as_getMutedDP()

    def as_getSearchDPS(self):
        """
        :return Object:
        """
        if self._isDAAPIInited():
            return self.flashObject.as_getSearchDP()

    def as_setSearchResultTextS(self, message):
        """
        :param message:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setSearchResultText(message)

    def as_frozenSearchActionS(self, flag):
        """
        :param flag:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_frozenSearchAction(flag)