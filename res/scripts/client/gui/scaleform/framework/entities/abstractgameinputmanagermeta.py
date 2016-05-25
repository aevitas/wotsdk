# Embedded file name: scripts/client/gui/Scaleform/framework/entities/abstract/GameInputManagerMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIModule import BaseDAAPIModule

class GameInputManagerMeta(BaseDAAPIModule):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIModule
    null
    """

    def handleGlobalKeyEvent(self, keyCode, eventType):
        """
        :param keyCode:
        :param eventType:
        :return :
        """
        self._printOverrideError('handleGlobalKeyEvent')

    def as_addKeyHandlerS(self, keyCode, eventType, ignoreText, cancelEventType):
        """
        :param keyCode:
        :param eventType:
        :param ignoreText:
        :param cancelEventType:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_addKeyHandler(keyCode, eventType, ignoreText, cancelEventType)

    def as_clearKeyHandlerS(self, keyCode, eventType):
        """
        :param keyCode:
        :param eventType:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_clearKeyHandler(keyCode, eventType)