# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/BrowserWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class BrowserWindowMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    """

    def as_configureS(self, title, showActionBtn, showCloseBtn):
        if self._isDAAPIInited():
            return self.flashObject.as_configure(title, showActionBtn, showCloseBtn)

    def as_setSizeS(self, width, height):
        if self._isDAAPIInited():
            return self.flashObject.as_setSize(width, height)