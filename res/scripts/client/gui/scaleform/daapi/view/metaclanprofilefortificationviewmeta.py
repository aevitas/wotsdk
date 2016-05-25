# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/ClanProfileFortificationViewMeta.py
from gui.Scaleform.daapi.view.lobby.clans.profile.ClanProfileBaseView import ClanProfileBaseView

class ClanProfileFortificationViewMeta(ClanProfileBaseView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends ClanProfileBaseView
    null
    """

    def as_showBodyDummyS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_showBodyDummy(data)

    def as_hideBodyDummyS(self):
        """
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_hideBodyDummy()