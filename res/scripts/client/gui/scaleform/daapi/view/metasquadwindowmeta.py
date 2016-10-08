# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/SquadWindowMeta.py
from gui.Scaleform.daapi.view.lobby.rally.BaseRallyMainWindow import BaseRallyMainWindow

class SquadWindowMeta(BaseRallyMainWindow):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseRallyMainWindow
    """

    def as_setComponentIdS(self, componentId):
        if self._isDAAPIInited():
            return self.flashObject.as_setComponentId(componentId)

    def as_setWindowTitleS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setWindowTitle(value)