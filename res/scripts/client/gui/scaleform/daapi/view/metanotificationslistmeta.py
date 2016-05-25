# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/NotificationsListMeta.py
from gui.Scaleform.daapi.view.lobby.popover.SmartPopOverView import SmartPopOverView

class NotificationsListMeta(SmartPopOverView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends SmartPopOverView
    null
    """

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

    def as_setInitDataS(self, value):
        """
        :param value:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setInitData(value)

    def as_setMessagesListS(self, value):
        """
        :param value:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setMessagesList(value)

    def as_appendMessageS(self, messageData):
        """
        :param messageData:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_appendMessage(messageData)

    def as_updateMessageS(self, messageData):
        """
        :param messageData:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_updateMessage(messageData)