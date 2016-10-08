# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/StatsBaseMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class StatsBaseMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    """

    def acceptSquad(self, uid):
        self._printOverrideError('acceptSquad')

    def addToSquad(self, uid):
        self._printOverrideError('addToSquad')

    def as_setIsIntaractiveS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setIsIntaractive(value)