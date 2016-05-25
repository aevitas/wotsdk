# Embedded file name: scripts/client/messenger/gui/Scaleform/meta/ChannelWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class ChannelWindowMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    null
    """

    def showFAQWindow(self):
        """
        :return :
        """
        self._printOverrideError('showFAQWindow')

    def getClientID(self):
        """
        :return Number:
        """
        self._printOverrideError('getClientID')

    def as_setTitleS(self, title):
        """
        :param title:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setTitle(title)

    def as_setCloseEnabledS(self, enabled):
        """
        :param enabled:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setCloseEnabled(enabled)