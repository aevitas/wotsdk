# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/FortSettingsPeripheryPopoverMeta.py
from gui.Scaleform.daapi.view.lobby.popover.SmartPopOverView import SmartPopOverView

class FortSettingsPeripheryPopoverMeta(SmartPopOverView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends SmartPopOverView
    """

    def onApply(self, server):
        self._printOverrideError('onApply')

    def as_setDataS(self, data):
        """
        :param data: Represented by PeripheryPopoverVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)

    def as_setTextsS(self, data):
        """
        :param data: Represented by PeripheryPopoverVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setTexts(data)