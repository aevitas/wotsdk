# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/FortCalendarWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class FortCalendarWindowMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    """

    def as_updatePreviewDataS(self, data):
        """
        :param data: Represented by FortCalendarPreviewBlockVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_updatePreviewData(data)