# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/FortSettingsDefenceHourPopoverMeta.py
from gui.Scaleform.daapi.view.lobby.popover.SmartPopOverView import SmartPopOverView

class FortSettingsDefenceHourPopoverMeta(SmartPopOverView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends SmartPopOverView
    null
    """

    def onApply(self, hour):
        """
        :param hour:
        :return :
        """
        self._printOverrideError('onApply')

    def as_setDataS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)

    def as_setTextsS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setTexts(data)