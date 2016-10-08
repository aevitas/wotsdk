# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/CrewOperationsPopOverMeta.py
from gui.Scaleform.daapi.view.lobby.popover.SmartPopOverView import SmartPopOverView

class CrewOperationsPopOverMeta(SmartPopOverView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends SmartPopOverView
    """

    def invokeOperation(self, operationName):
        self._printOverrideError('invokeOperation')

    def as_updateS(self, data):
        """
        :param data: Represented by CrewOperationsInitVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_update(data)