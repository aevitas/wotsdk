# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/NotificationPopUpViewerMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class NotificationPopUpViewerMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    null
    """

    def setListClear(self):
        """
        :return :
        """
        self._printOverrideError('setListClear')

    def onMessageHided(self, byTimeout, wasNotified):
        """
        :param byTimeout:
        :param wasNotified:
        :return :
        """
        self._printOverrideError('onMessageHided')

    def onClickAction(self, typeID, entityID, action):
        """
        :param typeID:
        :param entityID:
        :param action:
        :return :
        """
        self._printOverrideError('onClickAction')

    def getMessageActualTime(self, msTime):
        """
        :param msTime:
        :return String:
        """
        self._printOverrideError('getMessageActualTime')

    def as_hasPopUpIndexS(self, typeID, entityID):
        """
        :param typeID:
        :param entityID:
        :return Boolean:
        """
        if self._isDAAPIInited():
            return self.flashObject.as_hasPopUpIndex(typeID, entityID)

    def as_appendMessageS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_appendMessage(data)

    def as_updateMessageS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_updateMessage(data)

    def as_removeMessageS(self, typeID, entityID):
        """
        :param typeID:
        :param entityID:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_removeMessage(typeID, entityID)

    def as_removeAllMessagesS(self):
        """
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_removeAllMessages()

    def as_layoutInfoS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_layoutInfo(data)

    def as_initInfoS(self, maxMessagessCount, padding):
        """
        :param maxMessagessCount:
        :param padding:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_initInfo(maxMessagessCount, padding)