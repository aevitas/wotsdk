# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/FortFixedPlayersWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class FortFixedPlayersWindowMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    null
    """

    def assignToBuilding(self):
        """
        :return :
        """
        self._printOverrideError('assignToBuilding')

    def as_setWindowTitleS(self, value):
        """
        :param value:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setWindowTitle(value)

    def as_setDataS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)