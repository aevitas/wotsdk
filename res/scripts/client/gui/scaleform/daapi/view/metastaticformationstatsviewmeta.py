# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/StaticFormationStatsViewMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class StaticFormationStatsViewMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    """

    def selectSeason(self, index):
        self._printOverrideError('selectSeason')

    def as_setDataS(self, data):
        """
        :param data: Represented by StaticFormationStatsViewVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)

    def as_setStatsS(self, data):
        """
        :param data: Represented by StaticFormationStatsVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setStats(data)