# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/FortPeriodDefenceWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class FortPeriodDefenceWindowMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    null
    """

    def onApply(self, data):
        """
        :param data:
        :return :
        """
        self._printOverrideError('onApply')

    def onCancel(self):
        """
        :return :
        """
        self._printOverrideError('onCancel')

    def as_setDataS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)

    def as_setInitDataS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setInitData(data)