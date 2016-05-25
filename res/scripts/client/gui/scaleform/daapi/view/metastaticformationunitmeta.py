# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/StaticFormationUnitMeta.py
from gui.Scaleform.daapi.view.lobby.rally.BaseRallyRoomView import BaseRallyRoomView

class StaticFormationUnitMeta(BaseRallyRoomView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseRallyRoomView
    null
    """

    def toggleStatusRequest(self):
        """
        :return :
        """
        self._printOverrideError('toggleStatusRequest')

    def setRankedMode(self, isRanked):
        """
        :param isRanked:
        :return :
        """
        self._printOverrideError('setRankedMode')

    def showTeamCard(self):
        """
        :return :
        """
        self._printOverrideError('showTeamCard')

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

    def as_setLegionnairesCountS(self, visible, legionnairesCount):
        """
        :param visible:
        :param legionnairesCount:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setLegionnairesCount(visible, legionnairesCount)

    def as_setHeaderDataS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setHeaderData(data)

    def as_setTeamIconS(self, icon):
        """
        :param icon:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setTeamIcon(icon)