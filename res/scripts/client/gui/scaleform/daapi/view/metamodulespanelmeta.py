# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/ModulesPanelMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class ModulesPanelMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    """

    def showModuleInfo(self, moduleId):
        self._printOverrideError('showModuleInfo')

    def as_setDataS(self, data):
        """
        :param data: Represented by DevicesDataVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)

    def as_setVehicleHasTurretS(self, hasTurret):
        if self._isDAAPIInited():
            return self.flashObject.as_setVehicleHasTurret(hasTurret)

    def as_setModulesEnabledS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setModulesEnabled(value)