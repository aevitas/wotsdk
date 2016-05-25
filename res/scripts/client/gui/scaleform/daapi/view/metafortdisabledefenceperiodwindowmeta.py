# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/FortDisableDefencePeriodWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class FortDisableDefencePeriodWindowMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    null
    """

    def onClickApplyButton(self):
        """
        :return :
        """
        self._printOverrideError('onClickApplyButton')

    def as_setDataS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)