# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/CyberSportUnitsListMeta.py
from gui.Scaleform.daapi.view.lobby.rally.BaseRallyListView import BaseRallyListView

class CyberSportUnitsListMeta(BaseRallyListView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseRallyListView
    null
    """

    def getTeamData(self, index):
        """
        :param index:
        :return Object:
        """
        self._printOverrideError('getTeamData')

    def refreshTeams(self):
        """
        :return :
        """
        self._printOverrideError('refreshTeams')

    def filterVehicles(self):
        """
        :return :
        """
        self._printOverrideError('filterVehicles')

    def setTeamFilters(self, showOnlyStatic):
        """
        :param showOnlyStatic:
        :return :
        """
        self._printOverrideError('setTeamFilters')

    def loadPrevious(self):
        """
        :return :
        """
        self._printOverrideError('loadPrevious')

    def loadNext(self):
        """
        :return :
        """
        self._printOverrideError('loadNext')

    def showRallyProfile(self, id):
        """
        :param id:
        :return :
        """
        self._printOverrideError('showRallyProfile')

    def searchTeams(self, name):
        """
        :param name:
        :return :
        """
        self._printOverrideError('searchTeams')

    def as_setDummyS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setDummy(data)

    def as_setDummyVisibleS(self, visible):
        """
        :param visible:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setDummyVisible(visible)

    def as_setSearchResultTextS(self, text, descrText, filterData):
        """
        :param text:
        :param descrText:
        :param filterData:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setSearchResultText(text, descrText, filterData)

    def as_setHeaderS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setHeader(data)

    def as_updateNavigationBlockS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_updateNavigationBlock(data)

    def as_updateRallyIconS(self, iconPath):
        """
        :param iconPath:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_updateRallyIcon(iconPath)