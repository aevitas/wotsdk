# Embedded file name: scripts/client/messenger/gui/Scaleform/meta/ConnectToSecureChannelWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class ConnectToSecureChannelWindowMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    null
    """

    def sendPassword(self, value):
        """
        :param value:
        :return :
        """
        self._printOverrideError('sendPassword')

    def cancelPassword(self):
        """
        :return :
        """
        self._printOverrideError('cancelPassword')

    def as_infoMessageS(self, value):
        """
        :param value:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_infoMessage(value)