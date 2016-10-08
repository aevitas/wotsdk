# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/BattleMessageListMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIModule import BaseDAAPIModule

class BattleMessageListMeta(BaseDAAPIModule):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIModule
    """

    def onRefreshComplete(self):
        self._printOverrideError('onRefreshComplete')

    def as_setupListS(self, data):
        """
        :param data: Represented by FadingMessageListSettingsVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setupList(data)

    def as_clearS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_clear()

    def as_refreshS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_refresh()

    def as_showYellowMessageS(self, key, text):
        if self._isDAAPIInited():
            return self.flashObject.as_showYellowMessage(key, text)

    def as_showRedMessageS(self, key, text):
        if self._isDAAPIInited():
            return self.flashObject.as_showRedMessage(key, text)

    def as_showPurpleMessageS(self, key, text):
        if self._isDAAPIInited():
            return self.flashObject.as_showPurpleMessage(key, text)

    def as_showGreenMessageS(self, key, text):
        if self._isDAAPIInited():
            return self.flashObject.as_showGreenMessage(key, text)

    def as_showGoldMessageS(self, key, text):
        if self._isDAAPIInited():
            return self.flashObject.as_showGoldMessage(key, text)

    def as_showSelfMessageS(self, key, text):
        if self._isDAAPIInited():
            return self.flashObject.as_showSelfMessage(key, text)