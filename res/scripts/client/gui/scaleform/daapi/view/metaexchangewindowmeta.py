# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/ExchangeWindowMeta.py
from gui.Scaleform.daapi.view.lobby.exchange.BaseExchangeWindow import BaseExchangeWindow

class ExchangeWindowMeta(BaseExchangeWindow):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseExchangeWindow
    null
    """

    def as_setSecondaryCurrencyS(self, credits):
        """
        :param credits:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setSecondaryCurrency(credits)

    def as_setWalletStatusS(self, walletStatus):
        """
        :param walletStatus:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setWalletStatus(walletStatus)