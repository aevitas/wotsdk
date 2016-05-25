# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/QuestsTabMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class QuestsTabMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    null
    """

    def as_setQuestsDataS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setQuestsData(data)

    def as_setSelectedQuestS(self, questID):
        """
        :param questID:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setSelectedQuest(questID)