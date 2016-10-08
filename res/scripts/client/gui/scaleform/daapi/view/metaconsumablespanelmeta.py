# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/ConsumablesPanelMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class ConsumablesPanelMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    """

    def onClickedToSlot(self, keyCode):
        self._printOverrideError('onClickedToSlot')

    def onPopUpClosed(self):
        self._printOverrideError('onPopUpClosed')

    def as_setKeysToSlotsS(self, slots):
        if self._isDAAPIInited():
            return self.flashObject.as_setKeysToSlots(slots)

    def as_setItemQuantityInSlotS(self, idx, quantity):
        if self._isDAAPIInited():
            return self.flashObject.as_setItemQuantityInSlot(idx, quantity)

    def as_setItemTimeQuantityInSlotS(self, idx, quantity, timeRemaining, maxTime):
        if self._isDAAPIInited():
            return self.flashObject.as_setItemTimeQuantityInSlot(idx, quantity, timeRemaining, maxTime)

    def as_setCoolDownTimeS(self, idx, timeRemaining):
        if self._isDAAPIInited():
            return self.flashObject.as_setCoolDownTime(idx, timeRemaining)

    def as_setCoolDownPosAsPercentS(self, idx, percent):
        if self._isDAAPIInited():
            return self.flashObject.as_setCoolDownPosAsPercent(idx, percent)

    def as_addShellSlotS(self, idx, keyCode, sfKeyCode, quantity, clipCapacity, shellIconPath, noShellIconPath, tooltipText):
        if self._isDAAPIInited():
            return self.flashObject.as_addShellSlot(idx, keyCode, sfKeyCode, quantity, clipCapacity, shellIconPath, noShellIconPath, tooltipText)

    def as_setNextShellS(self, idx):
        if self._isDAAPIInited():
            return self.flashObject.as_setNextShell(idx)

    def as_setCurrentShellS(self, idx):
        if self._isDAAPIInited():
            return self.flashObject.as_setCurrentShell(idx)

    def as_addEquipmentSlotS(self, idx, keyCode, sfKeyCode, tag, quantity, timeRemaining, iconPath, tooltipText):
        if self._isDAAPIInited():
            return self.flashObject.as_addEquipmentSlot(idx, keyCode, sfKeyCode, tag, quantity, timeRemaining, iconPath, tooltipText)

    def as_showEquipmentSlotsS(self, show):
        if self._isDAAPIInited():
            return self.flashObject.as_showEquipmentSlots(show)

    def as_expandEquipmentSlotS(self, idx, slots):
        if self._isDAAPIInited():
            return self.flashObject.as_expandEquipmentSlot(idx, slots)

    def as_collapseEquipmentSlotS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_collapseEquipmentSlot()

    def as_addOptionalDeviceSlotS(self, idx, timeRemaining, iconPath, tooltipText):
        if self._isDAAPIInited():
            return self.flashObject.as_addOptionalDeviceSlot(idx, timeRemaining, iconPath, tooltipText)

    def as_addOrderSlotS(self, idx, keyCode, sfKeyCode, quantity, iconPath, tooltipText, available, quantityVisible, timeRemaining, maxTime):
        if self._isDAAPIInited():
            return self.flashObject.as_addOrderSlot(idx, keyCode, sfKeyCode, quantity, iconPath, tooltipText, available, quantityVisible, timeRemaining, maxTime)

    def as_setOrderAvailableS(self, idx, available):
        if self._isDAAPIInited():
            return self.flashObject.as_setOrderAvailable(idx, available)

    def as_setOrderActivatedS(self, idx):
        if self._isDAAPIInited():
            return self.flashObject.as_setOrderActivated(idx)

    def as_showOrdersSlotsS(self, show):
        if self._isDAAPIInited():
            return self.flashObject.as_showOrdersSlots(show)

    def as_isVisibleS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_isVisible()

    def as_resetS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_reset()

    def as_switchToPosmortemS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_switchToPosmortem()

    def as_updateEntityStateS(self, entityName, entityState):
        if self._isDAAPIInited():
            return self.flashObject.as_updateEntityState(entityName, entityState)