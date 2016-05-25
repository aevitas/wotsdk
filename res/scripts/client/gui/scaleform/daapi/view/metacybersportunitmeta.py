# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/CyberSportUnitMeta.py
from gui.Scaleform.daapi.view.lobby.rally.BaseRallyRoomView import BaseRallyRoomView

class CyberSportUnitMeta(BaseRallyRoomView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseRallyRoomView
    null
    """

    def toggleFreezeRequest(self):
        """
        :return :
        """
        self._printOverrideError('toggleFreezeRequest')

    def toggleStatusRequest(self):
        """
        :return :
        """
        self._printOverrideError('toggleStatusRequest')

    def showSettingsRoster(self, vaue):
        """
        :param vaue:
        :return :
        """
        self._printOverrideError('showSettingsRoster')

    def resultRosterSlotsSettings(self, value):
        """
        :param value:
        :return :
        """
        self._printOverrideError('resultRosterSlotsSettings')

    def cancelRosterSlotsSettings(self):
        """
        :return :
        """
        self._printOverrideError('cancelRosterSlotsSettings')

    def lockSlotRequest(self, slotIndex):
        """
        :param slotIndex:
        :return :
        """
        self._printOverrideError('lockSlotRequest')

    def as_updateSlotSettingsS(self, value):
        """
        :param value:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_updateSlotSettings(value)

    def as_closeSlotS(self, slotIdx, cost, slotsLabel):
        """
        :param slotIdx:
        :param cost:
        :param slotsLabel:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_closeSlot(slotIdx, cost, slotsLabel)

    def as_openSlotS(self, slotIdx, canBeTaken, slotsLabel, compatibleVehiclesCount):
        """
        :param slotIdx:
        :param canBeTaken:
        :param slotsLabel:
        :param compatibleVehiclesCount:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_openSlot(slotIdx, canBeTaken, slotsLabel, compatibleVehiclesCount)

    def as_lockUnitS(self, isLocked, slotsLabel):
        """
        :param isLocked:
        :param slotsLabel:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_lockUnit(isLocked, slotsLabel)

    def as_setOpenedS(self, isOpened, statusLabel):
        """
        :param isOpened:
        :param statusLabel:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setOpened(isOpened, statusLabel)

    def as_setTotalLabelS(self, hasTotalLevelError, totalLevelLabel, totalLevel):
        """
        :param hasTotalLevelError:
        :param totalLevelLabel:
        :param totalLevel:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setTotalLabel(hasTotalLevelError, totalLevelLabel, totalLevel)

    def as_setPlayerCountLblS(self, value):
        """
        :param value:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setPlayerCountLbl(value)