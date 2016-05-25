# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/SwitchModePanelMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class SwitchModePanelMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    null
    """

    def switchMode(self):
        """
        :return :
        """
        self._printOverrideError('switchMode')

    def onSelectCheckBoxAutoSquad(self, isSelected):
        """
        :param isSelected:
        :return :
        """
        self._printOverrideError('onSelectCheckBoxAutoSquad')

    def as_setDataS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)

    def as_setVisibleS(self, value):
        """
        :param value:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setVisible(value)