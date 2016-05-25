# Embedded file name: scripts/client/gui/Scaleform/framework/entities/abstract/FlashTweenMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIModule import BaseDAAPIModule

class FlashTweenMeta(BaseDAAPIModule):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIModule
    null
    """

    def moveOnPositionS(self, percent):
        """
        :param percent:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.moveOnPosition(percent)