# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/FortCreateDirectionWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class FortCreateDirectionWindowMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    null
    """

    def openNewDirection(self):
        """
        :return :
        """
        self._printOverrideError('openNewDirection')

    def closeDirection(self, id):
        """
        :param id:
        :return :
        """
        self._printOverrideError('closeDirection')

    def as_setDescriptionS(self, value):
        """
        :param value:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setDescription(value)

    def as_setupButtonS(self, enabled, visible, tooltip):
        """
        :param enabled:
        :param visible:
        :param tooltip:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setupButton(enabled, visible, tooltip)

    def as_setDirectionsS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setDirections(data)