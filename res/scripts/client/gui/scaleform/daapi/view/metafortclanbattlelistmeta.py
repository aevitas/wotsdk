# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/FortClanBattleListMeta.py
from gui.Scaleform.daapi.view.lobby.rally.BaseRallyListView import BaseRallyListView

class FortClanBattleListMeta(BaseRallyListView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseRallyListView
    null
    """

    def as_setClanBattleDataS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setClanBattleData(data)

    def as_upateClanBattlesCountS(self, value):
        """
        :param value:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_upateClanBattlesCount(value)