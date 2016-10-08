# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/QuestsCurrentTabMeta.py
from gui.Scaleform.daapi.view.lobby.server_events.QuestsTab import QuestsTab

class QuestsCurrentTabMeta(QuestsTab):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends QuestsTab
    """

    def sort(self, type, hideDone):
        self._printOverrideError('sort')

    def getSortedTableData(self, tableData):
        self._printOverrideError('getSortedTableData')

    def getQuestInfo(self, questID):
        self._printOverrideError('getQuestInfo')

    def collapse(self, id):
        self._printOverrideError('collapse')

    def as_showNoDataS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_showNoData()

    def as_showWaitingS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_showWaiting(value)

    def as_showNoSelectS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_showNoSelect()

    def as_updateQuestInfoS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_updateQuestInfo(data)

    def as_setSelectedQuestS(self, questID):
        if self._isDAAPIInited():
            return self.flashObject.as_setSelectedQuest(questID)