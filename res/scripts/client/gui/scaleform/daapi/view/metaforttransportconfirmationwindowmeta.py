# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/FortTransportConfirmationWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class FortTransportConfirmationWindowMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    null
    """

    def onCancel(self):
        """
        :return :
        """
        self._printOverrideError('onCancel')

    def onTransporting(self, size):
        """
        :param size:
        :return :
        """
        self._printOverrideError('onTransporting')

    def as_setMaxTransportingSizeS(self, maxSizeStr):
        """
        :param maxSizeStr:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setMaxTransportingSize(maxSizeStr)

    def as_setFooterTextS(self, text):
        """
        :param text:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setFooterText(text)

    def as_setDataS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)

    def as_enableForFirstTransportingS(self, isFirstTransporting):
        """
        :param isFirstTransporting:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_enableForFirstTransporting(isFirstTransporting)