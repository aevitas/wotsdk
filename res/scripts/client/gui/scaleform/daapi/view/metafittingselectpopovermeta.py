# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/FittingSelectPopoverMeta.py
from gui.Scaleform.daapi.view.lobby.popover.SmartPopOverView import SmartPopOverView

class FittingSelectPopoverMeta(SmartPopOverView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends SmartPopOverView
    """

    def setVehicleModule(self, newId, oldId, isRemove):
        self._printOverrideError('setVehicleModule')

    def showModuleInfo(self, moduleId):
        self._printOverrideError('showModuleInfo')

    def as_updateS(self, data):
        """
        :param data: Represented by FittingSelectPopoverVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_update(data)