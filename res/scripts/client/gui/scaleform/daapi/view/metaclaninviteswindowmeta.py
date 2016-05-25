# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/ClanInvitesWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class ClanInvitesWindowMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    null
    """

    def onInvitesButtonClick(self):
        """
        :return :
        """
        self._printOverrideError('onInvitesButtonClick')

    def as_setDataS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)

    def as_setClanInfoS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setClanInfo(data)

    def as_setHeaderStateS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setHeaderState(data)

    def as_setClanEmblemS(self, source):
        """
        :param source:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setClanEmblem(source)

    def as_setControlsEnabledS(self, enabled):
        """
        :param enabled:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setControlsEnabled(enabled)