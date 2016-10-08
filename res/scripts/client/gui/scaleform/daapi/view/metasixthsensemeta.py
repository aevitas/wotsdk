# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/SixthSenseMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class SixthSenseMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    """

    def as_showS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_show()

    def as_hideS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_hide()