# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/ConfirmModuleWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class ConfirmModuleWindowMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    null
    """

    def submit(self, count, currency):
        """
        :param count:
        :param currency:
        :return :
        """
        self._printOverrideError('submit')

    def as_setDataS(self, value):
        """
        :param value:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setData(value)

    def as_setSettingsS(self, value):
        """
        :param value:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setSettings(value)