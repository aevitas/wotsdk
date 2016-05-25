# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/TutorialHangarQuestDetailsMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class TutorialHangarQuestDetailsMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    null
    """

    def requestQuestInfo(self, questID):
        """
        :param questID:
        :return :
        """
        self._printOverrideError('requestQuestInfo')

    def showTip(self, id, type):
        """
        :param id:
        :param type:
        :return :
        """
        self._printOverrideError('showTip')

    def getSortedTableData(self, data):
        """
        :param data:
        :return Object:
        """
        self._printOverrideError('getSortedTableData')

    def as_updateQuestInfoS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_updateQuestInfo(data)