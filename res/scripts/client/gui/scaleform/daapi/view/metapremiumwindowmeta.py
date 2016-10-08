# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/PremiumWindowMeta.py
from gui.Scaleform.daapi.view.meta.SimpleWindowMeta import SimpleWindowMeta

class PremiumWindowMeta(SimpleWindowMeta):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends SimpleWindowMeta
    """

    def onRateClick(self, rateId):
        self._printOverrideError('onRateClick')

    def as_setHeaderS(self, prc, bonus1, bonus2):
        if self._isDAAPIInited():
            return self.flashObject.as_setHeader(prc, bonus1, bonus2)

    def as_setRatesS(self, data):
        """
        :param data: Represented by PremiumWindowRatesVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setRates(data)