# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/EliteWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class EliteWindowMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    null
    """

    def as_setVehicleS(self, vehicle):
        """
        :param vehicle:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setVehicle(vehicle)