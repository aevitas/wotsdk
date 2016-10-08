# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/ClanProfileTableStatisticsViewMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class ClanProfileTableStatisticsViewMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    """

    def as_setDataS(self, data):
        """
        :param data: Represented by ClanProfileTableStatisticsDataVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)

    def as_setAdditionalTextS(self, visible, text):
        if self._isDAAPIInited():
            return self.flashObject.as_setAdditionalText(visible, text)

    def as_getDPS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_getDP()