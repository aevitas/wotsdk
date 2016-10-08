# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/CyberSportUnitsListMeta.py
from gui.Scaleform.daapi.view.lobby.rally.BaseRallyListView import BaseRallyListView

class CyberSportUnitsListMeta(BaseRallyListView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseRallyListView
    """

    def getTeamData(self, index):
        self._printOverrideError('getTeamData')

    def refreshTeams(self):
        self._printOverrideError('refreshTeams')

    def filterVehicles(self):
        self._printOverrideError('filterVehicles')

    def setTeamFilters(self, showOnlyStatic):
        self._printOverrideError('setTeamFilters')

    def loadPrevious(self):
        self._printOverrideError('loadPrevious')

    def loadNext(self):
        self._printOverrideError('loadNext')

    def showRallyProfile(self, id):
        self._printOverrideError('showRallyProfile')

    def searchTeams(self, name):
        self._printOverrideError('searchTeams')

    def as_setDummyS(self, data):
        """
        :param data: Represented by DummyVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setDummy(data)

    def as_setDummyVisibleS(self, visible):
        if self._isDAAPIInited():
            return self.flashObject.as_setDummyVisible(visible)

    def as_setSearchResultTextS(self, text, descrText, filterData):
        if self._isDAAPIInited():
            return self.flashObject.as_setSearchResultText(text, descrText, filterData)

    def as_setHeaderS(self, data):
        """
        :param data: Represented by UnitListViewHeaderVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setHeader(data)

    def as_updateNavigationBlockS(self, data):
        """
        :param data: Represented by NavigationBlockVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_updateNavigationBlock(data)

    def as_updateRallyIconS(self, iconPath):
        if self._isDAAPIInited():
            return self.flashObject.as_updateRallyIcon(iconPath)