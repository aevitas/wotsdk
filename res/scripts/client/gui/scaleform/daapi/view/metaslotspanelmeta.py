# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/SlotsPanelMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class SlotsPanelMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    """

    def getSlotTooltipBody(self, orderID):
        self._printOverrideError('getSlotTooltipBody')

    def as_setPanelPropsS(self, data):
        """
        :param data: Represented by SlotsPanelPropsVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setPanelProps(data)

    def as_setSlotsS(self, orders):
        if self._isDAAPIInited():
            return self.flashObject.as_setSlots(orders)

    def as_updateSlotS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_updateSlot(data)