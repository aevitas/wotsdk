# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/ClanProfileGlobalMapInfoViewMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class ClanProfileGlobalMapInfoViewMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    """

    def as_setDataS(self, data):
        """
        :param data: Represented by ClanProfileGlobalMapInfoVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)