# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/ExchangeXpWindowMeta.py
from gui.Scaleform.daapi.view.lobby.exchange.BaseExchangeWindow import BaseExchangeWindow

class ExchangeXpWindowMeta(BaseExchangeWindow):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseExchangeWindow
    null
    """

    def as_vehiclesDataChangedS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_vehiclesDataChanged(data)

    def as_totalExperienceChangedS(self, value):
        """
        :param value:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_totalExperienceChanged(value)

    def as_setWalletStatusS(self, walletStatus):
        """
        :param walletStatus:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setWalletStatus(walletStatus)