# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/NotificationListButtonMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class NotificationListButtonMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    null
    """

    def handleClick(self):
        """
        :return :
        """
        self._printOverrideError('handleClick')

    def as_setStateS(self, isBlinking):
        """
        :param isBlinking:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setState(isBlinking)