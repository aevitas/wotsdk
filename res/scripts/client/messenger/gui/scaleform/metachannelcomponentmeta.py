# Embedded file name: scripts/client/messenger/gui/Scaleform/meta/ChannelComponentMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class ChannelComponentMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    """

    def isJoined(self):
        self._printOverrideError('isJoined')

    def sendMessage(self, message):
        self._printOverrideError('sendMessage')

    def getHistory(self):
        self._printOverrideError('getHistory')

    def getMessageMaxLength(self):
        self._printOverrideError('getMessageMaxLength')

    def onLinkClick(self, linkCode):
        self._printOverrideError('onLinkClick')

    def getLastUnsentMessage(self):
        self._printOverrideError('getLastUnsentMessage')

    def setLastUnsentMessage(self, message):
        self._printOverrideError('setLastUnsentMessage')

    def as_setJoinedS(self, flag):
        if self._isDAAPIInited():
            return self.flashObject.as_setJoined(flag)

    def as_addMessageS(self, message):
        if self._isDAAPIInited():
            return self.flashObject.as_addMessage(message)