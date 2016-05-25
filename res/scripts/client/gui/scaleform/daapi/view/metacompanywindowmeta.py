# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/CompanyWindowMeta.py
from gui.Scaleform.daapi.view.lobby.prb_windows.PrebattleWindow import PrebattleWindow

class CompanyWindowMeta(PrebattleWindow):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends PrebattleWindow
    null
    """

    def requestToAssign(self, pID):
        """
        :param pID:
        :return :
        """
        self._printOverrideError('requestToAssign')

    def requestToUnassign(self, pID):
        """
        :param pID:
        :return :
        """
        self._printOverrideError('requestToUnassign')

    def requestToChangeOpened(self, isOpened):
        """
        :param isOpened:
        :return :
        """
        self._printOverrideError('requestToChangeOpened')

    def requestToChangeComment(self, comment):
        """
        :param comment:
        :return :
        """
        self._printOverrideError('requestToChangeComment')

    def requestToChangeDivision(self, divisionID):
        """
        :param divisionID:
        :return :
        """
        self._printOverrideError('requestToChangeDivision')

    def getCompanyName(self):
        """
        :return String:
        """
        self._printOverrideError('getCompanyName')

    def canMoveToAssigned(self):
        """
        :return Boolean:
        """
        self._printOverrideError('canMoveToAssigned')

    def canMoveToUnassigned(self):
        """
        :return Boolean:
        """
        self._printOverrideError('canMoveToUnassigned')

    def canMakeOpenedClosed(self):
        """
        :return Boolean:
        """
        self._printOverrideError('canMakeOpenedClosed')

    def canChangeComment(self):
        """
        :return Boolean:
        """
        self._printOverrideError('canChangeComment')

    def canChangeDivision(self):
        """
        :return Boolean:
        """
        self._printOverrideError('canChangeDivision')

    def as_setDivisionsListS(self, data, selected):
        """
        :param data:
        :param selected:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setDivisionsList(data, selected)

    def as_setOpenedS(self, isOpened):
        """
        :param isOpened:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setOpened(isOpened)

    def as_setCommentS(self, comment):
        """
        :param comment:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setComment(comment)

    def as_setDivisionS(self, divisionID):
        """
        :param divisionID:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setDivision(divisionID)

    def as_setTotalLimitLabelsS(self, totalLevel, levelRange):
        """
        :param totalLevel:
        :param levelRange:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setTotalLimitLabels(totalLevel, levelRange)

    def as_setMaxCountLimitLabelS(self, label):
        """
        :param label:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setMaxCountLimitLabel(label)

    def as_setClassesLimitsS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setClassesLimits(data)

    def as_setInvalidVehiclesS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setInvalidVehicles(data)

    def as_setChangeSettingCoolDownS(self, coolDown):
        """
        :param coolDown:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setChangeSettingCoolDown(coolDown)