# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/CursorMeta.py
from gui.Scaleform.framework.entities.View import View

class CursorMeta(View):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends View
    """

    def as_setCursorS(self, cursor):
        if self._isDAAPIInited():
            return self.flashObject.as_setCursor(cursor)

    def as_showCursorS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_showCursor()

    def as_hideCursorS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_hideCursor()