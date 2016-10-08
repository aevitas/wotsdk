# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/TickerMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class TickerMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    """

    def showBrowser(self, entryID):
        self._printOverrideError('showBrowser')

    def as_setItemsS(self, items):
        if self._isDAAPIInited():
            return self.flashObject.as_setItems(items)