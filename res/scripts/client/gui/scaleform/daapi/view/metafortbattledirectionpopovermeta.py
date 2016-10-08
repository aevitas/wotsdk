# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/FortBattleDirectionPopoverMeta.py
from gui.Scaleform.daapi.view.lobby.popover.SmartPopOverView import SmartPopOverView

class FortBattleDirectionPopoverMeta(SmartPopOverView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends SmartPopOverView
    """

    def requestToJoin(self, fortBattleID):
        self._printOverrideError('requestToJoin')

    def as_setDataS(self, data):
        """
        :param data: Represented by BattleDirectionPopoverVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)