# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/ClanPersonalInvitesWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class ClanPersonalInvitesWindowMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    null
    """

    def as_setActualInvitesTextS(self, value):
        """
        :param value:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setActualInvitesText(value)

    def as_showWaitingAnimationS(self, value):
        """
        :param value:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_showWaitingAnimation(value)