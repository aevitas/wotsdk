# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/LegalInfoWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class LegalInfoWindowMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    null
    """

    def getLegalInfo(self):
        """
        :return :
        """
        self._printOverrideError('getLegalInfo')

    def onCancelClick(self):
        """
        :return :
        """
        self._printOverrideError('onCancelClick')

    def as_setLegalInfoS(self, legalInfo):
        """
        :param legalInfo:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setLegalInfo(legalInfo)