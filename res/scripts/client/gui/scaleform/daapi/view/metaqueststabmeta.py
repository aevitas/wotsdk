# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/QuestsTabMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class QuestsTabMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    """

    def as_setQuestsDataS(self, data):
        """
        :param data: Represented by QuestsDataVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setQuestsData(data)

    def as_setSelectedQuestS(self, questID):
        if self._isDAAPIInited():
            return self.flashObject.as_setSelectedQuest(questID)