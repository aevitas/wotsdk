# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/InputCheckerMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class InputCheckerMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    null
    """

    def sendUserInput(self, value, isValidSyntax):
        """
        :param value:
        :param isValidSyntax:
        :return :
        """
        self._printOverrideError('sendUserInput')

    def as_setTitleS(self, value):
        """
        :param value:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setTitle(value)

    def as_setBodyS(self, value):
        """
        :param value:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setBody(value)

    def as_setErrorMsgS(self, value):
        """
        :param value:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setErrorMsg(value)

    def as_setFormattedControlNumberS(self, value):
        """
        :param value:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setFormattedControlNumber(value)

    def as_setOriginalControlNumberS(self, value):
        """
        :param value:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setOriginalControlNumber(value)

    def as_invalidUserTextS(self, value):
        """
        :param value:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_invalidUserText(value)