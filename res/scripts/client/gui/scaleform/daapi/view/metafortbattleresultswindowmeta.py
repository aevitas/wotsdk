# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/FortBattleResultsWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class FortBattleResultsWindowMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    null
    """

    def getMoreInfo(self, battleID):
        """
        :param battleID:
        :return :
        """
        self._printOverrideError('getMoreInfo')

    def getClanEmblem(self):
        """
        :return :
        """
        self._printOverrideError('getClanEmblem')

    def as_setDataS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)

    def as_notAvailableInfoS(self, battleID):
        """
        :param battleID:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_notAvailableInfo(battleID)

    def as_setClanEmblemS(self, iconTag):
        """
        :param iconTag:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setClanEmblem(iconTag)