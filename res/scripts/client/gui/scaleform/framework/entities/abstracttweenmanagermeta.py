# Embedded file name: scripts/client/gui/Scaleform/framework/entities/abstract/TweenManagerMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIModule import BaseDAAPIModule

class TweenManagerMeta(BaseDAAPIModule):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIModule
    null
    """

    def createTween(self, tween):
        """
        :param tween:
        :return :
        """
        self._printOverrideError('createTween')

    def disposeTween(self, tween):
        """
        :param tween:
        :return :
        """
        self._printOverrideError('disposeTween')

    def disposeAll(self):
        """
        :return :
        """
        self._printOverrideError('disposeAll')

    def as_setDataFromXmlS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setDataFromXml(data)