# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/TankCarouselMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class TankCarouselMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    null
    """

    def vehicleChange(self, vehicleInventoryId):
        """
        :param vehicleInventoryId:
        :return :
        """
        self._printOverrideError('vehicleChange')

    def buySlot(self):
        """
        :return :
        """
        self._printOverrideError('buySlot')

    def buyTankClick(self):
        """
        :return :
        """
        self._printOverrideError('buyTankClick')

    def setVehiclesFilterOld(self, nation, vehicleType, favoriteSelected, gameModeSelected):
        """
        :param nation:
        :param vehicleType:
        :param favoriteSelected:
        :param gameModeSelected:
        :return :
        """
        self._printOverrideError('setVehiclesFilterOld')

    def setVehiclesFilter(self, bonusSelected, favoriteSelected, gameModeSelected):
        """
        :param bonusSelected:
        :param favoriteSelected:
        :param gameModeSelected:
        :return :
        """
        self._printOverrideError('setVehiclesFilter')

    def resetFilters(self):
        """
        :return :
        """
        self._printOverrideError('resetFilters')

    def setVehicleSelected(self, vehicleInventoryId, selected):
        """
        :param vehicleInventoryId:
        :param selected:
        :return :
        """
        self._printOverrideError('setVehicleSelected')

    def moveVehiclesSelectionSlot(self, vehicleInventoryId):
        """
        :param vehicleInventoryId:
        :return :
        """
        self._printOverrideError('moveVehiclesSelectionSlot')

    def as_setMultiselectionModeS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setMultiselectionMode(data)

    def as_setMultiselectionButtonLabelsS(self, activateLabel, deactivateLabel, disabledTooltip):
        """
        :param activateLabel:
        :param deactivateLabel:
        :param disabledTooltip:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setMultiselectionButtonLabels(activateLabel, deactivateLabel, disabledTooltip)

    def as_updateMultiselectionDataS(self, multiselectData):
        """
        :param multiselectData:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_updateMultiselectionData(multiselectData)

    def as_setCarouselFilterOldS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setCarouselFilterOld(data)

    def as_initCarouselFilterOldS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_initCarouselFilterOld(data)

    def as_setCarouselFilterS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setCarouselFilter(data)

    def as_initCarouselFilterS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_initCarouselFilter(data)

    def as_showCounterS(self, countText, isAttention):
        """
        :param countText:
        :param isAttention:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_showCounter(countText, isAttention)

    def as_hideCounterS(self):
        """
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_hideCounter()

    def as_blinkCounterS(self):
        """
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_blinkCounter()

    def as_setParamsS(self, params):
        """
        :param params:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setParams(params)

    def as_updateVehiclesS(self, vehiclesData, isSet):
        """
        :param vehiclesData:
        :param isSet:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_updateVehicles(vehiclesData, isSet)

    def as_showVehiclesS(self, compactDescrList):
        """
        :param compactDescrList:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_showVehicles(compactDescrList)