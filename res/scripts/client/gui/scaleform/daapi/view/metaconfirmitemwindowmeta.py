# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/ConfirmItemWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class ConfirmItemWindowMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    """

    def submit(self, count, currency):
        self._printOverrideError('submit')

    def as_setDataS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setData(value)

    def as_setSettingsS(self, data):
        """
        :param data: Represented by DialogSettingsVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setSettings(data)