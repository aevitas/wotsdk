# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/TankCarouselFilterPopoverMeta.py
from gui.Scaleform.daapi.view.lobby.popover.SmartPopOverView import SmartPopOverView

class TankCarouselFilterPopoverMeta(SmartPopOverView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends SmartPopOverView
    null
    """

    def changeFilter(self, groupId, itemId):
        """
        :param groupId:
        :param itemId:
        :return :
        """
        self._printOverrideError('changeFilter')

    def setDefaultFilter(self):
        """
        :return :
        """
        self._printOverrideError('setDefaultFilter')

    def as_setInitDataS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setInitData(data)

    def as_setStateS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setState(data)

    def as_enableDefBtnS(self, value):
        """
        :param value:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_enableDefBtn(value)