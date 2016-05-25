# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/FortIntelFilterMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class FortIntelFilterMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    null
    """

    def onTryToSearchByClanAbbr(self, tag, searchType):
        """
        :param tag:
        :param searchType:
        :return String:
        """
        self._printOverrideError('onTryToSearchByClanAbbr')

    def onClearClanTagSearch(self):
        """
        :return :
        """
        self._printOverrideError('onClearClanTagSearch')

    def as_setDataS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)

    def as_setMaxClanAbbreviateLengthS(self, length):
        """
        :param length:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setMaxClanAbbreviateLength(length)

    def as_setSearchResultS(self, status):
        """
        :param status:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setSearchResult(status)

    def as_setFilterStatusS(self, filterStatus):
        """
        :param filterStatus:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setFilterStatus(filterStatus)

    def as_setFilterButtonStatusS(self, filterButtonStatus, showEffect):
        """
        :param filterButtonStatus:
        :param showEffect:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setFilterButtonStatus(filterButtonStatus, showEffect)

    def as_setupCooldownS(self, isOnCooldown):
        """
        :param isOnCooldown:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setupCooldown(isOnCooldown)

    def as_setClanAbbrevS(self, clanAbbrev):
        """
        :param clanAbbrev:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setClanAbbrev(clanAbbrev)