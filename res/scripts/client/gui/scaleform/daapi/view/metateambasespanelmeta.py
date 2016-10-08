# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/TeamBasesPanelMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class TeamBasesPanelMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    """

    def as_addS(self, barId, sortWeight, colorType, title, points, captureTime, vehiclesCount):
        if self._isDAAPIInited():
            return self.flashObject.as_add(barId, sortWeight, colorType, title, points, captureTime, vehiclesCount)

    def as_removeS(self, id):
        if self._isDAAPIInited():
            return self.flashObject.as_remove(id)

    def as_stopCaptureS(self, id, points):
        if self._isDAAPIInited():
            return self.flashObject.as_stopCapture(id, points)

    def as_updateCaptureDataS(self, id, points, rate, captureTime, vehiclesCount):
        if self._isDAAPIInited():
            return self.flashObject.as_updateCaptureData(id, points, rate, captureTime, vehiclesCount)

    def as_setCapturedS(self, id, title):
        if self._isDAAPIInited():
            return self.flashObject.as_setCaptured(id, title)

    def as_setOffsetForEnemyPointsS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_setOffsetForEnemyPoints()

    def as_clearS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_clear()