# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/StoreComponentMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class StoreComponentMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    """

    def requestTableData(self, nation, type, filters):
        self._printOverrideError('requestTableData')

    def requestFilterData(self, filterType):
        self._printOverrideError('requestFilterData')

    def onShowInfo(self, itemCD):
        self._printOverrideError('onShowInfo')

    def getName(self):
        self._printOverrideError('getName')

    def onAddVehToCompare(self, itemCD):
        self._printOverrideError('onAddVehToCompare')

    def as_setNationsS(self, nations):
        if self._isDAAPIInited():
            return self.flashObject.as_setNations(nations)

    def as_completeInitS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_completeInit()

    def as_updateS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_update()

    def as_setFilterTypeS(self, data):
        """
        :param data: Represented by ShopNationFilterData (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setFilterType(data)

    def as_setSubFilterS(self, data):
        """
        :param data: Represented by ShopSubFilterData (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setSubFilter(data)

    def as_setFilterOptionsS(self, data):
        """
        :param data: Represented by FiltersDataVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setFilterOptions(data)

    def as_setVehicleCompareAvailableS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setVehicleCompareAvailable(value)