# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/BattleDAAPIComponentMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class BattleDAAPIComponentMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    """

    def as_populateS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_populate()

    def as_disposeS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_dispose()