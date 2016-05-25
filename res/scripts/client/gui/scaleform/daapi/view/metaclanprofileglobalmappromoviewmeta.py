# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/ClanProfileGlobalMapPromoViewMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class ClanProfileGlobalMapPromoViewMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    null
    """

    def showInfo(self):
        """
        :return :
        """
        self._printOverrideError('showInfo')

    def showMap(self):
        """
        :return :
        """
        self._printOverrideError('showMap')

    def as_setDataS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)