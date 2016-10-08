# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/MissionAwardWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class MissionAwardWindowMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    """

    def onCurrentQuestClick(self):
        self._printOverrideError('onCurrentQuestClick')

    def onNextQuestClick(self):
        self._printOverrideError('onNextQuestClick')

    def as_setDataS(self, data):
        """
        :param data: Represented by MissionAwardWindowVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)