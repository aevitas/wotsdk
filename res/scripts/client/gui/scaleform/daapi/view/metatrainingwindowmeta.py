# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/TrainingWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class TrainingWindowMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    """

    def updateTrainingRoom(self, key, time, isPrivate, description):
        self._printOverrideError('updateTrainingRoom')

    def as_setDataS(self, info, mapsData):
        if self._isDAAPIInited():
            return self.flashObject.as_setData(info, mapsData)