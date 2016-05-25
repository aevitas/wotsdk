# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/ModulesPanelMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class ModulesPanelMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    null
    """

    def setVehicleModule(self, newId, slotIdx, oldId, isRemove):
        """
        :param newId:
        :param slotIdx:
        :param oldId:
        :param isRemove:
        :return :
        """
        self._printOverrideError('setVehicleModule')

    def showModuleInfo(self, moduleId):
        """
        :param moduleId:
        :return :
        """
        self._printOverrideError('showModuleInfo')

    def as_setDataS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)

    def as_setVehicleHasTurretS(self, hasTurret):
        """
        :param hasTurret:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setVehicleHasTurret(hasTurret)

    def as_setModulesEnabledS(self, value):
        """
        :param value:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setModulesEnabled(value)