# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/QuestsControlMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class QuestsControlMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    """

    def showQuestsWindow(self):
        self._printOverrideError('showQuestsWindow')

    def as_setDataS(self, data):
        """
        :param data: Represented by QuestsControlBtnVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)