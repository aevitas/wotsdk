# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/ClanProfileFortificationInfoViewMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class ClanProfileFortificationInfoViewMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    """

    def as_setFortDataS(self, data):
        """
        :param data: Represented by ClanProfileFortificationViewVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setFortData(data)

    def as_setDataS(self, data):
        """
        :param data: Represented by ClanProfileFortificationViewInitVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)