# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/BaseExchangeWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class BaseExchangeWindowMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    null
    """

    def exchange(self, data):
        """
        :param data:
        :return :
        """
        self._printOverrideError('exchange')

    def as_setPrimaryCurrencyS(self, value):
        """
        :param value:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setPrimaryCurrency(value)

    def as_exchangeRateS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_exchangeRate(data)