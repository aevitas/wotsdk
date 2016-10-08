# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/BaseExchangeWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class BaseExchangeWindowMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    """

    def exchange(self, data):
        self._printOverrideError('exchange')

    def as_setPrimaryCurrencyS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setPrimaryCurrency(value)

    def as_exchangeRateS(self, data):
        """
        :param data: Represented by BaseExchangeWindowRateVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_exchangeRate(data)