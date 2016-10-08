# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/IconPriceDialogMeta.py
from gui.Scaleform.daapi.view.dialogs.IconDialog import IconDialog

class IconPriceDialogMeta(IconDialog):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends IconDialog
    """

    def as_setMessagePriceS(self, price, currency, actionPriceData):
        if self._isDAAPIInited():
            return self.flashObject.as_setMessagePrice(price, currency, actionPriceData)

    def as_setPriceLabelS(self, label):
        if self._isDAAPIInited():
            return self.flashObject.as_setPriceLabel(label)

    def as_setOperationAllowedS(self, isAllowed):
        if self._isDAAPIInited():
            return self.flashObject.as_setOperationAllowed(isAllowed)