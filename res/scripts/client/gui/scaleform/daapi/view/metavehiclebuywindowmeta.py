# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/VehicleBuyWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class VehicleBuyWindowMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    null
    """

    def submit(self, data):
        """
        :param data:
        :return :
        """
        self._printOverrideError('submit')

    def storeSettings(self, expanded):
        """
        :param expanded:
        :return :
        """
        self._printOverrideError('storeSettings')

    def as_setGoldS(self, gold):
        """
        :param gold:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setGold(gold)

    def as_setCreditsS(self, value):
        """
        :param value:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setCredits(value)

    def as_setInitDataS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setInitData(data)

    def as_setEnabledSubmitBtnS(self, enabled):
        """
        :param enabled:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setEnabledSubmitBtn(enabled)