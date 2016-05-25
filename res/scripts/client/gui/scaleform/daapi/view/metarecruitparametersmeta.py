# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/RecruitParametersMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class RecruitParametersMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    null
    """

    def onNationChanged(self, nationID):
        """
        :param nationID:
        :return :
        """
        self._printOverrideError('onNationChanged')

    def onVehicleClassChanged(self, vehClass):
        """
        :param vehClass:
        :return :
        """
        self._printOverrideError('onVehicleClassChanged')

    def onVehicleChanged(self, vehID):
        """
        :param vehID:
        :return :
        """
        self._printOverrideError('onVehicleChanged')

    def onTankmanRoleChanged(self, roleID):
        """
        :param roleID:
        :return :
        """
        self._printOverrideError('onTankmanRoleChanged')

    def as_setVehicleClassDataS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setVehicleClassData(data)

    def as_setVehicleDataS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setVehicleData(data)

    def as_setTankmanRoleDataS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setTankmanRoleData(data)

    def as_setNationsDataS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setNationsData(data)