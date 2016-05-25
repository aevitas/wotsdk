# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/IconPriceDialogMeta.py
from gui.Scaleform.daapi.view.dialogs.IconDialog import IconDialog

class IconPriceDialogMeta(IconDialog):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends IconDialog
    null
    """

    def as_setMessagePriceS(self, price, currency, actionPriceData):
        """
        :param price:
        :param currency:
        :param actionPriceData:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setMessagePrice(price, currency, actionPriceData)

    def as_setPriceLabelS(self, label):
        """
        :param label:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setPriceLabel(label)

    def as_setOperationAllowedS(self, isAllowed):
        """
        :param isAllowed:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setOperationAllowed(isAllowed)