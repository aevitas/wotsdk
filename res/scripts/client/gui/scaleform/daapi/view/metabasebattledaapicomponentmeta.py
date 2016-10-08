# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/BaseBattleDAAPIComponentMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIModule import BaseDAAPIModule

class BaseBattleDAAPIComponentMeta(BaseDAAPIModule):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIModule
    """

    def registerFlashComponent(self, component, alias):
        """
        :param component: Represented by IDAAPIModule (AS)
        """
        self._printOverrideError('registerFlashComponent')

    def isFlashComponentRegistered(self, alias):
        self._printOverrideError('isFlashComponentRegistered')

    def unregisterFlashComponent(self, alias):
        self._printOverrideError('unregisterFlashComponent')

    def as_populateS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_populate()

    def as_disposeS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_dispose()