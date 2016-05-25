# Embedded file name: scripts/client/gui/Scaleform/framework/entities/abstract/BaseDAAPIComponentMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIModule import BaseDAAPIModule

class BaseDAAPIComponentMeta(BaseDAAPIModule):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIModule
    null
    """

    def registerFlashComponent(self, component, alias):
        """
        :param component:
        :param alias:
        :return :
        """
        self._printOverrideError('registerFlashComponent')

    def isFlashComponentRegistered(self, alias):
        """
        :param alias:
        :return Boolean:
        """
        self._printOverrideError('isFlashComponentRegistered')

    def unregisterFlashComponent(self, alias):
        """
        :param alias:
        :return :
        """
        self._printOverrideError('unregisterFlashComponent')

    def as_populateS(self):
        """
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_populate()

    def as_disposeS(self):
        """
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_dispose()