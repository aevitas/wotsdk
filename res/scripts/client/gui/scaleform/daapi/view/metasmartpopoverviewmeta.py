# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/SmartPopOverViewMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractPopOverView import AbstractPopOverView

class SmartPopOverViewMeta(AbstractPopOverView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractPopOverView
    null
    """

    def as_setPositionKeyPointS(self, valX, valY):
        """
        :param valX:
        :param valY:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setPositionKeyPoint(valX, valY)