# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/AmmunitionPanelMeta.py
from gui.Scaleform.daapi.view.meta.ModulesPanelMeta import ModulesPanelMeta

class AmmunitionPanelMeta(ModulesPanelMeta):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends ModulesPanelMeta
    null
    """

    def showTechnicalMaintenance(self):
        """
        :return :
        """
        self._printOverrideError('showTechnicalMaintenance')

    def showCustomization(self):
        """
        :return :
        """
        self._printOverrideError('showCustomization')

    def toRentContinue(self):
        """
        :return :
        """
        self._printOverrideError('toRentContinue')

    def as_setAmmoS(self, shells, stateWarning):
        """
        :param shells:
        :param stateWarning:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setAmmo(shells, stateWarning)

    def as_updateVehicleStatusS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_updateVehicleStatus(data)