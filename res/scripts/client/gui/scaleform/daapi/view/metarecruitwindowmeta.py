# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/RecruitWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class RecruitWindowMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    null
    """

    def updateVehicleClassDropdown(self, nation):
        """
        :param nation:
        :return :
        """
        self._printOverrideError('updateVehicleClassDropdown')

    def updateVehicleTypeDropdown(self, nation, vclass):
        """
        :param nation:
        :param vclass:
        :return :
        """
        self._printOverrideError('updateVehicleTypeDropdown')

    def updateRoleDropdown(self, nation, vclass, vtype):
        """
        :param nation:
        :param vclass:
        :param vtype:
        :return :
        """
        self._printOverrideError('updateRoleDropdown')

    def updateNationDropdown(self):
        """
        :return :
        """
        self._printOverrideError('updateNationDropdown')

    def buyTankman(self, nationID, typeID, role, studyType, slot):
        """
        :param nationID:
        :param typeID:
        :param role:
        :param studyType:
        :param slot:
        :return :
        """
        self._printOverrideError('buyTankman')

    def updateAllDropdowns(self, nationID, tankType, typeID, roleType):
        """
        :param nationID:
        :param tankType:
        :param typeID:
        :param roleType:
        :return :
        """
        self._printOverrideError('updateAllDropdowns')

    def as_setVehicleClassDropdownS(self, vehicleClassData):
        """
        :param vehicleClassData:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setVehicleClassDropdown(vehicleClassData)

    def as_setVehicleTypeDropdownS(self, vehicleTypeData):
        """
        :param vehicleTypeData:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setVehicleTypeDropdown(vehicleTypeData)

    def as_setRoleDropdownS(self, roleData):
        """
        :param roleData:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setRoleDropdown(roleData)

    def as_setCreditsChangedS(self, credits):
        """
        :param credits:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setCreditsChanged(credits)

    def as_setGoldChangedS(self, gold):
        """
        :param gold:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setGoldChanged(gold)

    def as_initDataS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_initData(data)

    def as_setNationsS(self, nationsData):
        """
        :param nationsData:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setNations(nationsData)

    def as_setAllDropdownsS(self, nationsData, vehicleClassData, vehicleTypeData, roleData):
        """
        :param nationsData:
        :param vehicleClassData:
        :param vehicleTypeData:
        :param roleData:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setAllDropdowns(nationsData, vehicleClassData, vehicleTypeData, roleData)