# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/TechnicalMaintenanceMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class TechnicalMaintenanceMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    null
    """

    def getEquipment(self, id1, currency1, id2, currency2, id3, currency3, installSlotIndex):
        """
        :param id1:
        :param currency1:
        :param id2:
        :param currency2:
        :param id3:
        :param currency3:
        :param installSlotIndex:
        :return :
        """
        self._printOverrideError('getEquipment')

    def repair(self):
        """
        :return :
        """
        self._printOverrideError('repair')

    def setRefillSettings(self, vehicleCompact, repair, shells, equipment):
        """
        :param vehicleCompact:
        :param repair:
        :param shells:
        :param equipment:
        :return :
        """
        self._printOverrideError('setRefillSettings')

    def showModuleInfo(self, moduleId):
        """
        :param moduleId:
        :return :
        """
        self._printOverrideError('showModuleInfo')

    def fillVehicle(self, needRepair, needAmmo, needEquipment, isPopulate, isUnload, isOrderChanged, shells, equipment):
        """
        :param needRepair:
        :param needAmmo:
        :param needEquipment:
        :param isPopulate:
        :param isUnload:
        :param isOrderChanged:
        :param shells:
        :param equipment:
        :return :
        """
        self._printOverrideError('fillVehicle')

    def updateEquipmentCurrency(self, equipmentIndex, currency):
        """
        :param equipmentIndex:
        :param currency:
        :return :
        """
        self._printOverrideError('updateEquipmentCurrency')

    def as_setDataS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)

    def as_setEquipmentS(self, installed, setup, modules):
        """
        :param installed:
        :param setup:
        :param modules:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setEquipment(installed, setup, modules)

    def as_onAmmoInstallS(self):
        """
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_onAmmoInstall()

    def as_setCreditsS(self, credits):
        """
        :param credits:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setCredits(credits)

    def as_setGoldS(self, gold):
        """
        :param gold:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setGold(gold)

    def as_resetEquipmentS(self, equipmentCD):
        """
        :param equipmentCD:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_resetEquipment(equipmentCD)