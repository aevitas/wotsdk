# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/ExchangeFreeToTankmanXpWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class ExchangeFreeToTankmanXpWindowMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    null
    """

    def apply(self):
        """
        :return :
        """
        self._printOverrideError('apply')

    def onValueChanged(self, data):
        """
        :param data:
        :return :
        """
        self._printOverrideError('onValueChanged')

    def calcValueRequest(self, value):
        """
        :param value:
        :return :
        """
        self._printOverrideError('calcValueRequest')

    def as_setInitDataS(self, value):
        """
        :param value:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setInitData(value)

    def as_setCalcValueResponseS(self, price, actionPriceData):
        """
        :param price:
        :param actionPriceData:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setCalcValueResponse(price, actionPriceData)

    def as_setWalletStatusS(self, walletStatus):
        """
        :param walletStatus:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setWalletStatus(walletStatus)