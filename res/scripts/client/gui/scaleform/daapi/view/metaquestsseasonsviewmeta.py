# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/QuestsSeasonsViewMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class QuestsSeasonsViewMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    null
    """

    def onShowAwardsClick(self):
        """
        :return :
        """
        self._printOverrideError('onShowAwardsClick')

    def onTileClick(self, tileID):
        """
        :param tileID:
        :return :
        """
        self._printOverrideError('onTileClick')

    def onSlotClick(self, slotID):
        """
        :param slotID:
        :return :
        """
        self._printOverrideError('onSlotClick')

    def as_setDataS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)

    def as_setSeasonsDataS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setSeasonsData(data)

    def as_setSlotsDataS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setSlotsData(data)