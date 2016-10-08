# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/FalloutBattlePageMeta.py
from gui.Scaleform.daapi.view.battle.classic.page import ClassicPage

class FalloutBattlePageMeta(ClassicPage):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends ClassicPage
    """

    def as_setPostmortemGasAtackInfoS(self, infoStr, respawnStr, showDeadIcon):
        if self._isDAAPIInited():
            return self.flashObject.as_setPostmortemGasAtackInfo(infoStr, respawnStr, showDeadIcon)

    def as_hidePostmortemGasAtackInfoS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_hidePostmortemGasAtackInfo()