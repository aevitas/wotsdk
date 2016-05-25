# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/CompaniesWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class CompaniesWindowMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    null
    """

    def createCompany(self):
        """
        :return :
        """
        self._printOverrideError('createCompany')

    def joinCompany(self, prbID):
        """
        :param prbID:
        :return :
        """
        self._printOverrideError('joinCompany')

    def getDivisionsList(self):
        """
        :return Array:
        """
        self._printOverrideError('getDivisionsList')

    def refreshCompaniesList(self, creatorMask, isNotInBattle, division):
        """
        :param creatorMask:
        :param isNotInBattle:
        :param division:
        :return :
        """
        self._printOverrideError('refreshCompaniesList')

    def requestPlayersList(self, prbID):
        """
        :param prbID:
        :return :
        """
        self._printOverrideError('requestPlayersList')

    def showFAQWindow(self):
        """
        :return :
        """
        self._printOverrideError('showFAQWindow')

    def getClientID(self):
        """
        :return Number:
        """
        self._printOverrideError('getClientID')

    def as_getCompaniesListDPS(self):
        """
        :return Object:
        """
        if self._isDAAPIInited():
            return self.flashObject.as_getCompaniesListDP()

    def as_showPlayersListS(self, index):
        """
        :param index:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_showPlayersList(index)

    def as_setDefaultFilterS(self, creatorMask, isNotInBattle, division):
        """
        :param creatorMask:
        :param isNotInBattle:
        :param division:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setDefaultFilter(creatorMask, isNotInBattle, division)

    def as_setRefreshCoolDownS(self, time):
        """
        :param time:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setRefreshCoolDown(time)

    def as_disableCreateButtonS(self, isDisable):
        """
        :param isDisable:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_disableCreateButton(isDisable)