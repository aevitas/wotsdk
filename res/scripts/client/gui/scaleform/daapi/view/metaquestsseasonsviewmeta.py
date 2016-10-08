# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/QuestsSeasonsViewMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class QuestsSeasonsViewMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    """

    def onShowAwardsClick(self):
        self._printOverrideError('onShowAwardsClick')

    def onTileClick(self, tileID):
        self._printOverrideError('onTileClick')

    def onSlotClick(self, slotID):
        self._printOverrideError('onSlotClick')

    def as_setDataS(self, data):
        """
        :param data: Represented by QuestsSeasonsViewVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)

    def as_setSeasonsDataS(self, data):
        """
        :param data: Represented by SeasonsDataVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setSeasonsData(data)

    def as_setSlotsDataS(self, data):
        """
        :param data: Represented by QuestSlotsDataVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setSlotsData(data)