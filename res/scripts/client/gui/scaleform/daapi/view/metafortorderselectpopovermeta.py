# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/FortOrderSelectPopoverMeta.py
from gui.Scaleform.daapi.view.lobby.popover.SmartPopOverView import SmartPopOverView

class FortOrderSelectPopoverMeta(SmartPopOverView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends SmartPopOverView
    null
    """

    def addOrder(self, orderID):
        """
        :param orderID:
        :return :
        """
        self._printOverrideError('addOrder')

    def removeOrder(self, orderID):
        """
        :param orderID:
        :return :
        """
        self._printOverrideError('removeOrder')

    def as_setDataS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)