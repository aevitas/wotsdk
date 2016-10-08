# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/VehiclePreviewMeta.py
from gui.Scaleform.framework.entities.View import View

class VehiclePreviewMeta(View):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends View
    """

    def closeView(self):
        self._printOverrideError('closeView')

    def onBackClick(self):
        self._printOverrideError('onBackClick')

    def onBuyOrResearchClick(self):
        self._printOverrideError('onBuyOrResearchClick')

    def onOpenInfoTab(self, index):
        self._printOverrideError('onOpenInfoTab')

    def onCompareClick(self):
        self._printOverrideError('onCompareClick')

    def as_setStaticDataS(self, data):
        """
        :param data: Represented by VehPreviewStaticDataVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setStaticData(data)

    def as_updateInfoDataS(self, data):
        """
        :param data: Represented by VehPreviewInfoPanelVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_updateInfoData(data)

    def as_updateVehicleStatusS(self, status):
        if self._isDAAPIInited():
            return self.flashObject.as_updateVehicleStatus(status)

    def as_updatePriceS(self, data):
        """
        :param data: Represented by VehPreviewPriceDataVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_updatePrice(data)

    def as_updateBuyButtonS(self, enable, label):
        if self._isDAAPIInited():
            return self.flashObject.as_updateBuyButton(enable, label)