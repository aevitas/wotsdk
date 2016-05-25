# Embedded file name: scripts/client/tutorial/gui/Scaleform/meta/TutorialBattleStatisticMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class TutorialBattleStatisticMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    null
    """

    def restart(self):
        """
        :return :
        """
        self._printOverrideError('restart')

    def showVideoDialog(self):
        """
        :return :
        """
        self._printOverrideError('showVideoDialog')

    def as_setDataS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)